# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| home/templates/home | [index.html](https://github.com/Karla-Stein/opsiflow/blob/main/home/templates/home/index.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2F#textarea) | ![screenshot](documentation/validation/home-html.jpeg) | Homepage does not require log-in, hence validated via URL |
| products/templates/products| [products.html](https://github.com/Karla-Stein/opsiflow/blob/main/products/templates/products/products.html) |[HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2Fproducts%2F#textarea) | ![screenshot](documentation/validation/products-html.jpeg) | Products page does not require log-in, hence validated via URL |
| products/templates/products| [product_detail.html](https://github.com/Karla-Stein/opsiflow/blob/main/products/templates/products/product_detail.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2Fproducts%2Fproduct_detail%2F4#textarea) | ![screenshot](documentation/validation/product-detail-html.jpeg) | Product details does not require log-in, hence validated via URL |
| templates/allauth/account| [login.html](https://github.com/Karla-Stein/opsiflow/blob/main/templates/allauth/account/login.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fproducts%2Fproduct_detail%2F4#textarea) | ![screenshot](documentation/validation/login-html.jpeg) | Log in page does not require log-in, hence validated via URL |
| templates/allauth/account | [signup.html](https://github.com/Karla-Stein/opsiflow/blob/main/templates/allauth/account/signup.html) |  [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2Faccounts%2Fsignup%2F#textarea) | ![screenshot](documentation/validation/signup-html.jpeg) | Sign up page does not require log-in, hence validated via URL |
| bag/templates/bag | [bag.html](https://github.com/Karla-Stein/opsiflow/blob/main/bag/templates/bag/bag.html) |  | ![screenshot](documentation/validation/bag-html.jpeg) | Log in required, hence validated by input. |
| checkout/templates/checkout | [checkout.html](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/templates/checkout/checkout.html) |  | ![screenshot](documentation/validation/checkout-html.jpeg) | Log in required, hence validated by input. |
| checkout/templates/checkout  | [checkout_success.html](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/templates/checkout/checkout_success.html) |  | ![screenshot](documentation/validation/checkout-success-html.jpeg) |Log in required, hence validated by input. |
| profiles/templates/profiles | [purchases.html](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/templates/profiles/purchases.html) |  | ![screenshot](documentation/validation/my-purchases-html.jpeg) |Log in required, hence validated by input. |
| profiles/templates/profiles | [profile.html](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/templates/profiles/profile.html) |  | ![screenshot](documentation/validation/my-details-html.jpeg) | Log in required, hence validated by input. |
| templates/allauth/account| [logout.html](https://github.com/Karla-Stein/opsiflow/blob/main/templates/allauth/account/logout.html) |  | ![screenshot](documentation/validation/logout-html.jpeg) |Log in required, hence validated by input. |
| checkout/templates/checkout/email | [purchase_confirmation.html](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/templates/checkout/emails/purchase_confirmation.html) |  | ![screenshot](documentation/validation/email-html.jpeg) | The email template was rendered locally and validated by direct input. |
| templates | [404.html](https://github.com/Karla-Stein/opsiflow/blob/main/templates/404.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2F404&checkerrorpages=yes#textarea )| ![screenshot](documentation/validation/404-html.jpeg) | 404 page does not require log-in, hence validated via URL |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [checkout.css](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/static/checkout/css/checkout.css) | [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=+https%3A%2F%2Fopsiflow.s3.amazonaws.com%2Fstatic%2Fcheckout%2Fcss%2Fcheckout.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/checkout-css.jpeg) | Passed with 0 errors and 0 warnings. |
| products | [product_detail.css](https://github.com/Karla-Stein/opsiflow/blob/main/products/static/products/css/product_detail.css) | [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fopsiflow.s3.amazonaws.com%2Fstatic%2Fproducts%2Fcss%2Fproduct_detail.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/product-details-css.jpeg) |  Passed with 0 errors. The validator reported 4 warnings relating to CSS custom variables, which are expected and do not affect functionality. |
| products | [products.css](https://github.com/Karla-Stein/opsiflow/blob/main/products/static/products/css/products.css) | [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=+https%3A%2F%2Fopsiflow.s3.amazonaws.com%2Fstatic%2Fproducts%2Fcss%2Fproducts.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/products-css.jpeg) |  Passed with 0 errors and 0 warnings. |
| profiles | [profiles.css](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/static/profiles/css/profiles.css) | [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fopsiflow.s3.amazonaws.com%2Fstatic%2Fprofiles%2Fcss%2Fprofiles.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/profiles-css.jpeg) | Passed with 0 errors. The validator reported 1 warning relating to CSS custom variables, which are expected and do not affect functionality. |
| static | [base.css](https://github.com/Karla-Stein/opsiflow/blob/main/static/css/base.css) | [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fopsiflow.s3.amazonaws.com%2Fstatic%2Fcss%2Fbase.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/base-css.jpeg) | Passed with 0 errors. The validator reported 23 warnings relating to CSS custom variables, which are expected and do not affect functionality. |


### Javascript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | [stripe.js](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/static/checkout/js/stripe.js) | ![screenshot](documentation/validation/js-checkout-stripe.jpeg) |  |
| products | [product_details.js](https://github.com/Karla-Stein/opsiflow/blob/main/products/static/products/js/product_details.js) | ![screenshot](documentation/validation/js-product-details.jpeg) |  |
| bag | [bag.html](https://github.com/Karla-Stein/opsiflow/blob/main/bag/templates/bag/bag.html) | ![screenshot](documentation/validation/js-bag.jpeg) | Embedded JavaScript snippet located in the postloadjs block. JSHint validation performed using ES11 and Bootstrap global configuration. |
| products | [products.html](https://github.com/Karla-Stein/opsiflow/blob/main/products/templates/products/products.html) | ![screenshot](documentation/validation/js-products.jpeg) |  Embedded JavaScript snippet located in the postloadjs block. JSHint validation performed using ES11 configuration. |
| templates | [base.html](https://github.com/Karla-Stein/opsiflow/blob/main/templates/base.html)| ![screenshot](documentation/validation/js-base.jpeg) |  Embedded JavaScript snippet located in the postloadjs block. JSHint validation performed using ES11 and Bootstrap global configuration. |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | 
| --- | --- | --- | --- | 
| bag | [contexts.py](https://github.com/Karla-Stein/opsiflow/blob/main/bag/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/bag/contexts.py) | ![screenshot](documentation/validation/py-bag-contexts.jpeg) | 
| bag | [test_views.py](https://github.com/Karla-Stein/opsiflow/blob/main/bag/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/bag/test_views.py) | ![screenshot](documentation/validation/py-bag-test-views.jpeg) |  
| bag | [urls.py](https://github.com/Karla-Stein/opsiflow/blob/main/bag/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/bag/urls.py) | ![screenshot](documentation/validation/py-bag-urls.jpeg) |  
| bag | [views.py](https://github.com/Karla-Stein/opsiflow/blob/main/bag/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/bag/views.py) | ![screenshot](documentation/validation/py-bag-views.jpeg) | 
| checkout | [admin.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/admin.py) | ![screenshot](documentation/validation/py-checkout-admin.jpeg) | 
| checkout | [forms.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/forms.py) | ![screenshot](documentation/validation/py-checkout-forms.jpeg) |  
| checkout | [models.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/models.py) | ![screenshot](documentation/validation/py-checkout-models.jpeg) | 
| checkout | [test_forms.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/test_forms.py) | ![screenshot](documentation/validation/py-checkout-test-forms.jpeg) | 
| checkout | [test_models.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/test_models.py) | ![screenshot](documentation/validation/py-checkout-test-models.jpeg) |  
| checkout | [test_views.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/test_views.py) | ![screenshot](documentation/validation//py-checkout-test-views.jpeg) | 
| checkout | [test_webhooks.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/test_webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/test_webhooks.py) | ![screenshot](documentation/validation/py-checkout-test-webhooks.jpeg) |  
| checkout | [urls.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/urls.py) | ![screenshot](documentation/validation/py-checkout-urls.jpeg) |  
| checkout | [views.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/views.py) | ![screenshot](documentation/validation/py-checkout-views.jpeg) | 
| checkout | [webhook_handler.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/py-checkout-webhook-handler.jpeg) | 
| checkout | [webhooks.py](https://github.com/Karla-Stein/opsiflow/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/checkout/webhooks.py) | ![screenshot](documentation/validation/py-checkout-webhooks.jpeg) | 
| home | [test_views.py](https://github.com/Karla-Stein/opsiflow/blob/main/home/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/home/test_views.py) | ![screenshot](documentation/validation/py-home-test-views.jpeg) |  
| home | [urls.py](https://github.com/Karla-Stein/opsiflow/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.jpeg) | 
| home | [views.py](https://github.com/Karla-Stein/opsiflow/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.jpeg) |  
| opsiflow | [settings.py](https://github.com/Karla-Stein/opsiflow/blob/main/opsiflow/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/opsiflow/settings.py) | ![screenshot](documentation/validation/py-opsiflow-settings.jpeg) |  
| opsiflow | [urls.py](https://github.com/Karla-Stein/opsiflow/blob/main/opsiflow/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/opsiflow/urls.py) | ![screenshot](documentation/validation/py-opsiflow-urls.jpeg) |  
| products | [admin.py](https://github.com/Karla-Stein/opsiflow/blob/main/products/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/products/admin.py) | ![screenshot](documentation/validation/py-products-admin.jpeg) | 
| products | [models.py](https://github.com/Karla-Stein/opsiflow/blob/main/products/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/products/models.py) | ![screenshot](documentation/validation/py-products-models.jpeg) | 
| products | [test_models.py](https://github.com/Karla-Stein/opsiflow/blob/main/products/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/products/test_models.py) | ![screenshot](documentation/validation/py-products-test-models.jpeg) | 
| products | [test_views.py](https://github.com/Karla-Stein/opsiflow/blob/main/products/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/products/test_views.py) | ![screenshot](documentation/validation/py-products-test-views.jpeg) | 
| products | [urls.py](https://github.com/Karla-Stein/opsiflow/blob/main/products/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/products/urls.py) | ![screenshot](documentation/validation/py-products-urls.jpeg) |  
| products | [views.py](https://github.com/Karla-Stein/opsiflow/blob/main/products/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/products/views.py) | ![screenshot](documentation/validation/py-products-views.jpeg) | 
| profiles | [admin.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/admin.py) | ![screenshot](documentation/validation/py-profiles-admin.jpeg) |  
| profiles | [forms.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/forms.py) | ![screenshot](documentation/validation/py-profiles-forms.jpeg) | 
| profiles | [models.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/models.py) | ![screenshot](documentation/validation/py-profiles-models.jpeg) |  
| profiles | [signals.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/signals.py) | ![screenshot](documentation/validation/py-profiles-signals.jpeg) |  
| profiles | [test_forms.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/test_forms.py) | ![screenshot](documentation/validation/py-profiles-test-forms.jpeg) | 
| profiles | [test_models.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/test_models.py) | ![screenshot](documentation/validation/py-profiles-test-model.jpeg) | 
| profiles | [test_views.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/test_views.py) | ![screenshot](documentation/validation/py-profiles-test-views.jpeg) | 
| profiles | [urls.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/urls.py) | ![screenshot](documentation/validation/py-profiles-urls.jpeg) |  
| profiles | [views.py](https://github.com/Karla-Stein/opsiflow/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/profiles/views.py) | ![screenshot](documentation/validation/py-profiles-views.jpeg) | 
|  | [custom_storages.py](https://github.com/Karla-Stein/opsiflow/blob/main/custom_storages.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/custom_storages.py) | ![screenshot](documentation/validation/py-custom-storages.jpeg) | 
|  | [manage.py](https://github.com/Karla-Stein/opsiflow/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/manage.py) | ![screenshot](documentation/validation/py-manage.jpeg) |  


### Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/responsiveness/mobile-home.jpeg) | ![screenshot](documentation/responsiveness/tablet-home.jpeg) | ![screenshot](documentation/responsiveness/desktop-home.jpeg) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.jpeg) | ![screenshot](documentation/responsiveness/tablet-products.jpeg) | ![screenshot](documentation/responsiveness/desktop-products.jpeg) | Works as expected |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-detail.jpeg) | ![screenshot](documentation/responsiveness/tablet-product-detail.jpeg) | ![screenshot](documentation/responsiveness/desktop-product-detail.jpeg) | Works as expected |
| Sign up | ![screenshot](documentation/responsiveness/mobile-signup.jpeg) | ![screenshot](documentation/responsiveness/tablet-signup.jpeg) | ![screenshot](documentation/responsiveness/desktop-signup.jpeg) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-signin.jpeg) | ![screenshot](documentation/responsiveness/tablet-signin.jpeg) | ![screenshot](documentation/responsiveness/desktop-signin.jpeg) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.jpeg) | ![screenshot](documentation/responsiveness/desktop-profile.jpeg) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.jpeg) | ![screenshot](documentation/responsiveness/tablet-bag.jpeg) | ![screenshot](documentation/responsiveness/desktop-bag.jpeg) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.jpeg) | ![screenshot](documentation/responsiveness/tablet-checkout.jpeg) | ![screenshot](documentation/responsiveness/desktop-checkout.jpeg) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.jpeg) | ![screenshot](documentation/responsiveness/tablet-checkout-success.jpeg) | ![screenshot](documentation/responsiveness/desktop-checkout-success.jpeg) | Works as expected |
| My Purchases | ![screenshot](documentation/responsiveness/mobile-purchases.jpeg) | ![screenshot](documentation/responsiveness/tablet-purchases.jpeg) | ![screenshot](documentation/responsiveness/desktop-purchases.jpeg) | Works as expected |
| Logout | ![screenshot](documentation/responsiveness/mobile-signout.jpeg) | ![screenshot](documentation/responsiveness/tablet-signout.jpeg) | ![screenshot](documentation/responsiveness/desktop-signout.jpeg) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.jpeg) | ![screenshot](documentation/responsiveness/desktop-404.jpeg) | Works as expected |







