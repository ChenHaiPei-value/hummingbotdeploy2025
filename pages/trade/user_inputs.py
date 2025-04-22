import streamlit as st
from typing import Tuple, Dict, List, Optional

def get_trade_inputs(credentials: Dict) -> Tuple[str, str, str, str, Optional[str]]:
    """获取交易表单输入"""
    col1, col2 = st.columns(2)
    
    with col1:
        # 交易所选择
        exchange = st.selectbox(
            "选择交易所",
            options=list(credentials.keys()),
            format_func=lambda x: x.upper()
        )
        
        # 交易对选择
        symbols = _get_symbols_for_exchange(credentials, exchange)
        symbol = st.selectbox(
            "选择交易对",
            options=symbols
        )
        
        # 买卖方向
        side = st.radio(
            "方向",
            options=["buy", "sell"],
            horizontal=True
        )
    
    with col2:
        # 数量输入
        amount = st.text_input(
            "数量",
            value="0.01",
            help="输入要交易的数量"
        )
        
        # 价格输入(可选)
        price = st.text_input(
            "价格(限价单必填)",
            value="",
            help="留空则为市价单"
        )
    
    return (exchange, symbol, side, amount, price if price else None)

def _get_symbols_for_exchange(credentials: Dict, exchange: str) -> List[str]:
    """获取指定交易所可用的交易对"""
    # TODO: 实际实现应从API获取
    # 这里返回一些常见交易对作为示例
    common_pairs = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT"]
    return common_pairs
