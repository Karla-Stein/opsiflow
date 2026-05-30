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




