# Checkout Process
1. Cart -> Checkout view
    ?
    - Login/Register or Enter an Email(as guest)
    - Shipping Address
    - Billing Info
        - Billing Address
        - Credit Card / Payment
 
2. Billing App/Component
    - Billing Profile
        - User or Email(guest Email)
        - generate payment processor token(Stripe or Braintee)
    
3. Orders / Invoices Component
    - Connecting the Billing Profile
    - Shipping / Billing Address
    - Cart
    - Status -- Shipped? Cancelled?
    