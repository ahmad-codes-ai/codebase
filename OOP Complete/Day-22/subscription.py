'''
Problem 10: Subscription Plan Manager
Context: A SaaS business needs to handle subscriptions.

Task: Create a Subscription class with:

Attributes: plan_name, monthly_fee.
Method:
upgrade(new_plan, new_fee) – change plan and fee.
Class variable: base_discount = 0.1 (10%).
Class method: apply_discount(fee) – return fee after discount.
Create a subscription, upgrade, compute discounted fee.
'''

class Subscription:
  base_discount = 0.1

  def __init__(self,plan,fee):
    self.plan = plan
    self.fee = fee

  def upgrade(self,np,nf):
    if np == self.plan:
      print("You are already on this plan")
    else:
      self.plan = np 
      self.fee = nf
      print("Your plan has been updated")

  @staticmethod
  def aplly_discount(fee):
    dis = fee * Subscription.base_discount
    fee-=dis
    print(f"Fee after discount: {fee}")

u1 = Subscription('basic',10)
u1.upgrade('pro',25)
Subscription.aplly_discount(u1.fee)