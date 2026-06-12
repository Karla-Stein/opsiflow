# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| home/templates/home | [index.html](https://github.com/Karla-Stein/opsiflow/blob/main/home/templates/home/index.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2F#textarea) | ![screenshot](documentation/validation/home-html.jpeg) | Homepage does not require log-in, hence validated via URL |
| home/templates/home | [contact.html](https://github.com/Karla-Stein/opsiflow/blob/main/home/templates/home/contact.html) | [HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fopsiflow-952bb478dd9c.herokuapp.com%2Fcontact%2F#textarea) | ![screenshot](documentation/validation/contact-html.jpeg) | Contact page does not require log-in, hence validated via URL |
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
| home | [forms.py](https://github.com/Karla-Stein/opsiflow/blob/main/home/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Karla-Stein/opsiflow/refs/heads/main/home/forms.py) | ![screenshot](documentation/validation/py-home-forms.jpeg) |  
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
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.jpeg) | ![screenshot](documentation/responsiveness/tablet-contact.jpeg) | ![screenshot](documentation/responsiveness/desktop-contact.jpeg) | Works as expected |
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


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/browsers/chrome-home.jpeg) | ![screenshot](documentation/browsers/firefox-home.jpeg) | ![screenshot](documentation/browsers/safari-home.jpeg) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.jpeg) | ![screenshot](documentation/browsers/firefox-contact.jpeg) | ![screenshot](documentation/browsers/safarai-contact.jpeg) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.jpeg) | ![screenshot](documentation/browsers/firefox-home.jpeg) | ![screenshot](documentation/browsers/safari-products.jpeg) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.jpeg) | ![screenshot](documentation/browsers/firefox-product-details.jpeg) | ![screenshot](documentation/browsers/safari-product-details.jpeg) | Works as expected |
| Sign Up | ![screenshot](documentation/browsers/chrome-signup.jpeg) | ![screenshot](documentation/browsers/firefox-signup.jpeg) | ![screenshot](documentation/browsers/safari-signup.jpeg) | Works as expected |
| Log In | ![screenshot](documentation/browsers/chrome-signin.jpeg) | ![screenshot](documentation/browsers/firefox-signin.jpeg) | ![screenshot](documentation/browsers/safari-signin.jpeg) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.jpeg) | ![screenshot](documentation/browsers/firefox-profile.jpeg) | ![screenshot](documentation/browsers/safari-profile.jpeg) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.jpeg) | ![screenshot](documentation/browsers/firefox-bag.jpeg) | ![screenshot](documentation/browsers/safari-bag.jpeg) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.jpeg) | ![screenshot](documentation/browsers/firefox-checkout.jpeg) | ![screenshot](documentation/browsers/safari-checkout.jpeg) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.jpeg) | ![screenshot](documentation/browsers/firefox-checkout-success.jpeg) | ![screenshot](documentation/browsers/safari-checkout-success.jpeg) | Works as expected |
| Purchases| ![screenshot](documentation/browsers/chrome-purchases.jpeg) | ![screenshot](documentation/browsers/firefox-purchases.jpeg) | ![screenshot](documentation/browsers/safari-purchases.jpeg) | Works as expected |
| Log Out | ![screenshot](documentation/browsers/chrome-signout.jpeg) | ![screenshot](documentation/browsers/firefox-signout.jpeg) | ![screenshot](documentation/browsers/safari-signout.jpeg) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.jpeg) | ![screenshot](documentation/browsers/firefox-404.jpeg) | ![screenshot](documentation/browsers/safari-404.jpeg) | Works as expected |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop | 
| --- | --- | --- | 
| Home | ![screenshot](documentation/lighthouse/mobile-home.jpeg) | ![screenshot](documentation/lighthouse/desktop-home.jpeg) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.jpeg) | ![screenshot](documentation/lighthouse/desktop-contact.jpeg) |
| Products | ![screenshot](documentation/lighthouse/mobile-products.jpeg) | ![screenshot](documentation/lighthouse/desktop-products.jpeg) |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-detail.jpeg) | ![screenshot](documentation/lighthouse/desktop-product-detail.jpeg) |
| Sign in | ![screenshot](documentation/lighthouse/mobile-signin.jpeg) | ![screenshot](documentation/lighthouse/desktop-signin.jpeg) |
| Sign up | ![screenshot](documentation/lighthouse/mobile-signup.jpeg) | ![screenshot](documentation/lighthouse/desktop-signup.jpeg) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.jpeg) | ![screenshot](documentation/lighthouse/desktop-bag.jpeg) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.jpeg) | ![screenshot](documentation/lighthouse/desktop-checkout.jpeg) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.jpeg) | ![screenshot](documentation/lighthouse/desktop-checkout-success.jpeg) |
| Purchases | ![screenshot](documentation/lighthouse/mobile-purchases.jpeg) | ![screenshot](documentation/lighthouse/desktop-purchases.jpeg) |
| Profiles | ![screenshot](documentation/lighthouse/mobile-profiles.jpeg) | ![screenshot](documentation/lighthouse/desktop-profile.jpeg) |
| Sign out | ![screenshot](documentation/lighthouse/mobile-signout.jpeg) | ![screenshot](documentation/lighthouse/desktop-signout.jpeg) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.jpeg) | ![screenshot](documentation/lighthouse/desktop-404.jpeg) |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Contact | Name field is required. | Omitted name input, tried to submit form. | Form was not submitted and visually highlighted missing input field. | ![screenshot](documentation/defensive/contact-name.jpeg) |
| | Email field is required. | Omitted email input and tried adding a name without the @ sign, then tried to submit. | Form was not submitted and visually highlighted missing input field. | ![screenshot](documentation/defensive/contact-email.jpeg) |
| | Subject field is required. | Omitted subject input, tried to submit form.  | Form was not submitted and visually highlighted missing input field. | ![screenshot](documentation/defensive/contact-subject.jpeg) |
| | Messege field is required. | Omitted message input, tried to submit form.  | Form was not submitted and visually highlighted missing input field. | ![screenshot](documentation/defensive/contact-mesage.jpeg) |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/features/product-browsing.jpeg) |
| | Feature is expected to sort products by price, name and complexity. | Tested sorting options for price (low-to-high/high-to-low), name (A-Z/Z-A) and complexity (low-to-high/high-to-low). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/name-a-z.jpeg) ![screenshot](documentation/defensive/name-z-z-a.jpeg) ![screenshot](documentation/defensive/complexity-high-low.jpeg) ![screenshot](documentation/defensive/complexity-low-high.jpeg) ![screenshot](documentation/defensive/price-high-low.jpeg) ![screenshot](documentation/defensive/price-low-high.jpeg)  |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/category-billing.jpeg)  ![screenshot](documentation/defensive/category-custom.jpeg)  ![screenshot](documentation/defensive/category-email.jpeg)  ![screenshot](documentation/defensive/category-lead.jpeg)|
| Product Details | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/features/product-details.jpeg) |
| | Feature is expected to display a description and price of the selected product option . | Clicked on both options on all product detail pages to view correct rendering of descriptions and price. | All product option descriptions and prices were displayed correctly. | ![screenshot](documentation/defensive/option-selector.jpeg) |
| | Feature is expected to prompt the log in requirement. | Clicked the 'Add to basket' button in logged out state. | A modal popped up prompting to either log in or sign up. | ![screenshot](documentation/defensive/login-modal.jpeg) |
| Bag| Feature is expected to prohibit multiple purchases of the same product. | Tried to add both options of the same product to the bag. | Adding was prohibited and warning received. | ![screenshot](documentation/defensive/multiple-product-warning.jpeg) |
| | Feature is expected to swap product option. | Added  product with option "Service Setup" to the bag, then clicked the change button in bag. | Product option was successfully swaped to "DIY Template" | ![screenshot](documentation/defensive/change-option.jpeg) |
| | Feature is expected to remove item from bag. | Clicked the bin icon button in bag. | Product was succeesfully removed from bag.| ![screenshot](documentation/defensive/remove-item.jpeg) ![screenshot](documentation/defensive/remove-item-success.jpeg)|
| | Feature is expected to restrict access to authenticated users only. | Attempted to access the bag page while logged out. | User was redirected to the login page and access was denied.| ![screenshot](documentation/defensive/restrict-bag.jpeg) |
| Checkout | Feature is expected to display bag items, order total, discounts, grand total, input fields for checkout and Stripe payment element. | Proceeded to checkout with items in the cart. | Checkout page displayed all content as expected. | ![screenshot](documentation/defensive/checkout-content.jpeg) |
| | Name field is required. | Omitted name input, tried to checkout with card details. | Order was not submitted and form visually highlighted missing input field. | ![screenshot](documentation/defensive/checkout-form-name.jpeg) |
| | Last Name field is required. | Omitted last name input, tried to checkout with card details. | Order was not submitted and form visually highlighted missing input field. | ![screenshot](documentation/defensive/checkout-form-lastname.jpeg) |
| | Email field is required. | Omitted email input, tried to checkout with card details. | Order was not submitted and form visually highlighted missing input field. | ![screenshot](documentation/defensive/checkout-form-email.jpeg) |
| | Street Address 1 field is required. | Omitted street address 1 input, tried to checkout with card details. | Order was not submitted and form visually highlighted missing input field. | ![screenshot](documentation/defensive/checkout-form-street.jpeg) |
| | City field is required. | Omitted city input, tried to checkout with card details. | Order was not submitted and form visually highlighted missing input field. | ![screenshot](documentation/defensive/checkout-form-city.jpeg) |
| | Country field is required. | Omitted country input, tried to checkout with card details. | Order was not submitted and form visually highlighted missing input field. | ![screenshot](documentation/defensive/checkou-form-country.jpeg) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid form and card details using Stripe at checkout. | Payment was processed securely and an order success page was displayed. | ![screenshot](documentation/defensive/success-page.jpeg) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/successpage-ordernumber.jpeg) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.jpeg) |
| | Feature is expected to restrict access to authenticated users only. | Attempted to access the checkout page while logged out. | User was redirected to the login page and access was denied.| ![screenshot](documentation/defensive/restrict-checkout.jpeg) |
| My Purchases | Feature is expected to allow returning customers to view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/purchases.jpeg) |
| | Feature is expected to restrict access to authenticated users only. | Attempted to access the my purchases page while logged out. | User was redirected to the login page and access was denied.| ![screenshot](documentation/defensive/restriction-purchases.jpeg) |
| | Feature is expected to restrict purchased DIY Templates to a maximum of three downloads per order. | Attempted to download the same DIY Template three times using the download links available on the checkout success page, My Purchases page and purchase confirmation email. | Downloads were successfully permitted up to the three-download limit. Any subsequent download attempts were blocked and an appropriate warning message was displayed.| ![screenshot](documentation/defensive/download-restriction.jpeg) |
| Profile Details | Feature is expected to allow logged-in users to update their saved personal details and reuse them during checkout. | Updated the user details form, saved the changes, then returned to the checkout form. | Updated details were saved successfully and automatically populated the checkout form. | ![screenshot](documentation/defensive/update-details-1.jpeg) ![screenshot](documentation/defensive/update-details-2.jpeg)|
| | Feature is expected to validate the email address format when an email address is provided. | Entered an invalid email address without an '@' symbol in the optional email field and attempted to save the profile. | The form prevented submission and displayed a validation warning, informing the user that a valid email address must be entered. | ![screenshot](documentation/defensive/email-validation.jpeg) |
| | Feature is expected to restrict access to authenticated users only. | Attempted to access the profile page while logged out. | User was redirected to the login page and access was denied.| ![screenshot](documentation/defensive/restriction-profile.jpeg) |
| Admin | Feature is expected to allow superusers to create products, product options and categories through the Django admin panel. | Logged in as a superuser and tested creating products, product options and categories. | Superuser was able to manage all product-related records successfully through the admin interface. | ![screenshot](documentation/defensive/create-category.jpeg) ![screenshot](documentation/defensive/create-product.jpeg) ![screenshot](documentation/defensive/create-option.jpeg) |
|  | Feature is expected to allow superusers to update products, product options and categories through the Django admin panel. | Logged in as a superuser and tested editing products, product options and categories. | Superuser was able to manage all product-related records successfully through the admin interface. | ![screenshot](documentation/defensive/update-category.jpeg) ![screenshot](documentation/defensive/update-product.jpeg) ![screenshot](documentation/defensive/update-option.jpeg) |
|  | Feature is expected to allow superusers to delete products, product options and categories through the Django admin panel. | Logged in as a superuser and tested deleting products, product options and categories. | Superuser was able to manage all product-related records successfully through the admin interface. | ![screenshot](documentation/defensive/delete-category.jpeg) ![screenshot](documentation/defensive/delete-product.jpeg) ![screenshot](documentation/defensive/delete-option.jpeg) |
| | Feature is expected to prevent tiered custom workflow services from being configured as downloadable products. | Attempted to save a ProductOption with fulfilment choice set to "Download" and a custom workflow tier selected. | The admin form prevented the invalid save and displayed the validation error: "You can not select fulfilment choice download for tiered services". | ![screenshot](documentation/defensive/product-option-validation-download-tier.jpeg) |
| | Feature is expected to require a downloadable file when a ProductOption is configured as a DIY Template. | Attempted to save a ProductOption with fulfilment choice set to "DIY Template" without uploading a download file. | The admin form prevented the invalid save and displayed the validation error: "You must choose a file." | ![screenshot](documentation/defensive/admin-download-file-validation.jpeg) |
| | Feature is expected to prevent downloadable files from being attached to ProductOptions configured as Set Up Services. | Attempted to save a ProductOption with fulfilment choice set to "Set Up Service" while uploading a download file. | The admin form prevented the invalid save and displayed the validation error: "You must not add a file." | ![screenshot](documentation/defensive/admin-service-file-validation.jpeg) |
| | Feature is expected to require delivery days when a ProductOption is configured as a Set Up Service. | Attempted to save a ProductOption with fulfilment choice set to "Set Up Service" without specifying delivery days. | The admin form prevented the invalid save and displayed the validation error: "You must add delivery days." | ![screenshot](documentation/defensive/admin-delivery-days-validation.jpeg) |
| | Feature is expected to prevent delivery days from being assigned to ProductOptions configured as DIY Templates. | Attempted to save a ProductOption with fulfilment choice set to "DIY Template" while specifying delivery days. | The admin form prevented the invalid save and displayed the validation error: "You must not add delivery days." | ![screenshot](documentation/defensive/admin-diy-delivery-days-validation.jpeg) |
| | Feature is expected to require delivery days when a custom workflow tier is selected. | Attempted to save a ProductOption with a custom workflow tier selected but without specifying delivery days. | The admin form prevented the invalid save and displayed the validation error: "You must add delivery days." | ![screenshot](documentation/defensive/admin-tier-delivery-days-validation.jpeg) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.jpeg) |


## Stripe Testing 

The Stripe integration was tested using Stripe test mode and test card details.
The following functionality was verified:

| Test | Result | Screenshot |
| --- | --- | --- |
| PaymentIntent created during checkout | Stripe creates a PaymentIntent with the correct amount | ![screenshot](documentation/stripe/payment-intent-created.jpeg) ![screenshot](documentation/stripe/payment-intent-created2.jpeg)  |
| PaymentIntent amount calculation | Amount matches selected product options. |  ![screenshot](documentation/stripe/payment-amount.jpeg) ![screenshot](documentation/stripe/payment-amount2.jpeg) |
| Successful card payment | Payment completes successfully |  ![screenshot](documentation/stripe/payment-success.jpeg) ![screenshot](documentation/stripe/payment-success2.jpeg) |
| Order creation after successful payment | Order is stored in the database with status confirmed |  ![screenshot](documentation/stripe/order-creation.jpeg) ![screenshot](documentation/stripe/order-creation2.jpeg) |
| Check card payments work | Expected charge succeeded with "card" in Stripe Event object | ![screenshot](documentation/stripe/card-payment.jpeg) |
| Check Revolut payments work | Expected charge succeeded with "revolut_pay" in Stripe Event object | ![screenshot](documentation/stripe/revolut-payment.jpeg) |
| Check Klarna payments work | Expected charge succeeded with "klarna" in Stripe Event object | ![screenshot](documentation/stripe/klarna-payments.jpeg) |
| Check Amazon Pay payments work | Expected charge succeeded with "amazon_pay" in Stripe Event object | ![screenshot](documentation/stripe/amazon-payments.jpeg) |
| Stripe webhook handling | Stripe webhook testing confirmed that `payment_intent.succeeded` events were delivered successfully to the deployed webhook endpoint. The application returned HTTP 200 and confirmed that the related order already existed in the database, demonstrating that the webhook handler correctly verifies completed payments without creating duplicate orders. | ![screenshot](documentation/stripe/webhook.jpeg) |


## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As an anonymous user | I want to land on a clear homepage | so that I understand what the platform offers.| ![screenshot](documentation/features/anonym-home.jpeg) |
| As an anonymous user | I want to browse available workflows | so that I can explore solutions before committing. |  ![screenshot](documentation/features/anonym-browse.jpeg) |
| As an anonymous user|  I want to view workflow details | so that I understand what each automation does. |  ![screenshot](documentation/features/anonym-product-detail.jpeg) |
| As an anonymous user| I want to create an account | so that I can use the websites features. | ![screenshot](documentation/features/signup.jpeg) |
| As a user | I want to log in securely | so that I can view my profile and purchases. | ![screenshot](documentation/features/signin.jpeg) |
| As a user | I can search for keywords | so that I quickly find what I am looking for.| ![screenshot](documentation/features/searchbar.jpeg) |
| As a user | I want to sort products by price, name and complexity | so that I can quickly find products that best match my budget and requirements. | ![screenshot](documentation/features/sorting.jpeg) |
| As a user | I want to contact OpsiFlow directly through the website | so that I can ask questions about products, services or custom workflow support. | ![screenshot](documentation/features/contact-form.jpeg) ![screenshot](documentation/features/contact-email.jpeg) |
| As a logged in user| I want to log out | so that my account remains secure. | ![screenshot](documentation/features/signout.jpeg) |
| As a logged in user | I want to add workflows to my bag | so that I can review before purchasing. | ![screenshot](documentation/features/add-to-basket.jpeg) |
| As a logged in user | I want to update or remove items from my bag | so that I stay in control of my purchase. | ![screenshot](documentation/features/update-remove-bag.jpeg) |
| As a logged in user | I want to checkout securely | so that I can complete my purchase with confidence. | ![screenshot](documentation/features/stripe.jpeg) |
| As a logged in user | I want to choose between template only or workflow & setup. | so that I can decide my level of support. | ![screenshot](documentation/features/product-option.jpeg) |
| As a logged in user | I want to download my purchased workflow | so that I can use it immediately. | ![screenshot](documentation/features/download-success.jpeg) ![screenshot](documentation/features/download-history.jpeg) ![screenshot](documentation/features/download-email.jpeg) |
| As a logged in user | I receive a confirmation email after purchase | so that I have a backup on instructions on how to proceed. | ![screenshot](documentation/features/confirmation-email.jpeg) |
| As a logged in user | I can navigate to my purchase history | so that I can view all my previous purchases in one place. | ![screenshot](documentation/features/purchase-history.jpeg) |
| As a logged in user | I can see a checkout confirmation | so that I can trust that the checkout process was successful. | ![screenshot](documentation/features/success-page.jpeg) |
| As a logged in user | I can update my profile | so that my profile is always accurate. | ![screenshot](documentation/features/profile-management.jpeg) |
| As a logged in user | I want to delete my account | so that I can stay in control of my data. | ![screenshot](documentation/features/delete-modal.jpeg) |
| As a site owner | I want to limit downloads | so that my products are not distributed freely. | ![screenshot](documentation/features/download-limit.jpeg) |
| As a site superuser | I want to create, view, update and delete products, product options and categories | so that I can keep the product catalogue accurate and up to date. | ![screenshot](documentation/features/product-admin.jpeg) |


## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I used Django’s built-in testing framework to verify the functionality of the application. Unit tests were written to test models, forms, views and business logic throughout the project.
To run the tests for a specific application, I used the following commands:

- python3 manage.py test bag
- python3 manage.py test checkout
- python3 manage.py test home
- python3 manage.py test products
- python3 manage.py test profiles

To run all tests across the project, I used:

- python3 manage.py test

### Coverage Testing

To measure the percentage of code covered by automated tests, I used the Coverage package.

Installation:

- pip install coverage

To generate the coverage report, I ran:

- coverage run --omit="*/migrations/*,*/__init__.py" manage.py test
- coverage report

To generate a detailed HTML coverage report, I ran:

- coverage html

Below are the results from the full coverage report on my application that I've tested before the Contact page implementation:

![screenshot](documentation/automation/html-coverage.jpeg)
![screenshot](documentation/automation/html-coverage-2.jpeg)


Following implementation of the contact form feature and associated automated tests, the overall project coverage increased by 1%.

The HTML coverage report was reviewed using the **"Hide Covered"** option. This filters out files that are already 100% covered and displays only files that still contain uncovered lines. This made it easier to identify where further testing could be improved.

![screenshot](documentation/automation/html-coverage-filtered.jpeg)


## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Karla-Stein/opsiflow?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/Karla-Stein/opsiflow/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)
I've used [GitHub Issues](https://www.github.com/Karla-Stein/opsiflow/issues) to document bugs.
All previously closed/fixed bugs can be tracked [here](https://www.github.com/Karla-Stein/opsiflow/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.jpeg)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Karla-Stein/opsiflow?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/Karla-Stein/opsiflow/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/Karla-Stein/opsiflow/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.jpeg)

## Known Issues

| Issue | Screenshot |
| --- | --- |
| Stripe displays a console recommendation suggesting migration from the current Payment Element integration to Stripe Checkout Sessions. The application uses Stripe's Payment Element successfully and all payment functionality operates as expected. The warning is informational only and does not indicate a fault within the application. Migrating to Checkout Sessions would require a significant architectural change and was considered outside the scope of the project. | ![screenshot](documentation/issues/stripe-api-recommendation.jpeg) |
| Stripe displays a console warning indicating that Klarna and Revolut Pay are not activated for live mode. Both payment methods were enabled and tested successfully in Stripe test mode. The warning remained despite activation and did not affect checkout functionality or Lighthouse scores. Core card payments and the implemented checkout flow operate correctly. | ![screenshot](documentation/issues/stripe-payment-method-activation.jpeg) |
| Stripe displays a console warning indicating that Apple Pay requires domain registration and verification before it can be enabled within the Payment Element. The project was developed and tested using Stripe test mode, where core card payment functionality operated correctly. Apple Pay was not required for the project's primary checkout functionality and domain verification was therefore considered outside the scope of the project. | ![screenshot](documentation/issues/apple-pay-domain-verification.jpeg) |
| Chrome DevTools reports missing `id` or `name` attributes within Stripe-controlled payment elements. Inspection confirmed that Django form fields include valid attributes. The warning originates from Stripe-generated elements which cannot be directly modified. | ![screenshot](documentation/issues/stripe-form-fields.jpeg) |
| Chrome DevTools reports a deprecated feature warning originating from a third-party script loaded by Stripe. The warning does not affect checkout functionality and cannot be addressed within the project codebase. | ![screenshot](documentation/issues/deprecated-third-party-script.jpeg) |
| Lighthouse Best Practices scores on the checkout page are affected by third-party cookies, Stripe scripts, Google Pay integrations and hCaptcha resources required for secure payment processing and fraud prevention. | ![screenshot](documentation/issues/third-party-cookies.jpeg) |
| Lighthouse continues to report document request latency, cache lifetime, render-blocking requests, font display, forced reflow, network dependency tree warnings and excessive preconnect suggestions. Investigation confirmed that these warnings primarily originate from hosting response times, third-party services, Stripe payment scripts, Bootstrap resources and other external dependencies rather than the project's application logic. The warnings do not affect the core functionality of the application and were therefore considered acceptable within the scope of the project. | ![screenshot](documentation/issues/lighthouse-third-party-warnings.jpeg) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.










