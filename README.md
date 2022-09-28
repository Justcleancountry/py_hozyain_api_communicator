Hozyain API python communicator
===============================

Package that helps to communicate with HOZYAIN.API

## Usage

```python
from hozyain_api_communicator import (
  HozyainAPIDataTypeBase,
  IHozyainAPIEndpoint,
  HozyainAPICommunicatorService
)


class LogPurchaseInControlPanelResponse(HozyainAPIDataTypeBase):
    success: bool


# This class will repsenent certain operation
class LogPurchaseInControlPanelWithoutFail(IHozyainAPIEndpoint):
    request = '''
mutation LogPurchaseInControlPanel {
  response: logPurchaseInControlPanel(
    authorTelegramId: "$author_telegram_id"
    authorTelegramUsername: "$author_telegram_username",
    productOrService: "$product_or_service",
    paymentMethod: "$payment_method",
    moneyAmount: $money_amount,
    controlPanelId: $control_panel_id,
  ) {
    success
  }
}
    '''
    response_type = LogPurchaseInControlPanelResponse

    @classmethod
    def transform_response(cls, response_to_transform: dict) -> dict:
        return response_to_transform['response']


if __name__ == '__main__':
  # Communicator class is singleton,
  # so you need to initialize it somewhere before using the service
  HozyainAPICommunicatorService(url='https://api.hozyain.me/graphql/')
  
  # After initializing, you can use operations that we have defined above
  LogPurchaseInControlPanelWithoutFail.make_request(
    author_telegram_id='123456789',
    author_telegram_username='some_telegram_username',
    product_or_service='Name of the service',
    payment_method='Cash',
    money_amount=15,
    control_panel_id=1,
  )
```
