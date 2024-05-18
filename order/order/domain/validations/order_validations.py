def validate_order(order):
    if order.total <= 0:
        raise ValueError("El total del pedido debe ser positivo.")
    if order.status not in ['Pagado', 'Creado', 'Enviado']:
        raise ValueError("Estatus de pedido no válido")
    if not order.order_products:
        raise ValueError("El pedido debe tener al menos un producto.")
