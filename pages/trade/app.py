import streamlit as st
from ..config.utils import get_backend_api_client
from .user_inputs import get_trade_inputs

def show_trade_page():
    st.title("交易所交易面板")
    
    # 获取可用交易所凭证
    client = get_backend_api_client()
    credentials = client.get_credentials()
    
    # 显示交易表单
    exchange, symbol, side, amount, price = get_trade_inputs(credentials)
    
    if st.button("提交订单"):
        try:
            # 调用API下单
            result = client.create_order(
                exchange=exchange,
                symbol=symbol,
                side=side,
                amount=float(amount),
                price=float(price) if price else None
            )
            st.success(f"订单提交成功! 订单ID: {result['order_id']}")
        except Exception as e:
            st.error(f"下单失败: {str(e)}")

    # 显示当前持仓
    if exchange and symbol:
        try:
            positions = client.get_positions(exchange, symbol)
            st.subheader("当前持仓")
            st.dataframe(positions)
        except Exception as e:
            st.warning(f"无法获取持仓: {str(e)}")
