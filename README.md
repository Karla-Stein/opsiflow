# [opsiflow](https://opsiflow-952bb478dd9c.herokuapp.com)

Developer: Karla Steinbrink ([Karla-Stein](https://www.github.com/Karla-Stein))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Karla-Stein/opsiflow)](https://www.github.com/Karla-Stein/opsiflow/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Karla-Stein/opsiflow)](https://www.github.com/Karla-Stein/opsiflow/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Karla-Stein/opsiflow)](https://www.github.com/Karla-Stein/opsiflow)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://opsiflow-952bb478dd9c.herokuapp.com)


PROJECT INTRODUCTION AND RATIONALE

Many businesses struggle with repetitive administrative tasks that reduce productivity and limit growth. This project is a web-based e-commerce platform designed to help entrepreneurs and small to medium-sized businesses streamline their operations through workflow automation. The platform allows users to explore automation concepts by browsing and purchasing ready-to-use workflow templates, which  serve as an accessible introduction to automation tools and processes. While these templates provide immediate practical value, the primary goal of the platform is to connect businesses with tailored automation solutions offered as a service. Users can therefore either implement templates independently using downloadable setup guides or request customised automation systems designed to meet their specific operational needs.


**Site Mockups**

![screenshot](documentation/mockup.jpeg)

source: [opsiflow amiresponsive](https://ui.dev/amiresponsive?url=https://opsiflow-952bb478dd9c.herokuapp.com)


## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

- Provide businesses with access to workflow automation templates and custom automation services to reduce repetitive administrative tasks.
- Offer an intuitive platform where users can explore, understand and implement automation solutions to improve efficiency and productivity.

**Primary User Needs**

- Business owners need simple and ready-to-use automation templates to quickly streamline repetitive processes.
- Users seeking advanced solutions need access to tailored automation services that fit their specific operational requirements.
- All users need a clear and user-friendly platform to browse automations, understand their benefits and complete secure purchases.

**Business Goals**

- Position the platform as a reliable source for automation solutions.
- Convert users from template buyers into higher-value service clients.
- Demonstrate the value of automation in improving efficiency, scalability and time management for businesses.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**

- Backend product management (create, update, delete and display workflow templates and service offerings).
- Public home page.
- Public product browsing page.
- Search and sort functionality.
- Detailed product pages with clear descriptions, benefits and options to choose from.
- User account functionality (register, log in, log out, view purchase history and manage profile details).
- A log in required purchase process. 
- Secure checkout system with the ability to add, update, or remove items from a shopping bag.
- Digital product delivery (downloadable templates with setup instructions and email confirmation).
- Download limitation system to restrict distribution of purchased templates.
- Order confirmation and success pages for both digital downloads and service bookings.
- 404 error page to handle invalid or broken URLs.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
    - Links to Home, Workflows, Shopping Bag, My Purchases, My Details, Account deletion and authentication pages (Sign Up, Sign In and Sign Out).
    - Authenticated users can access their purchase history and secure download area through the profile section.
    - Superusers have access to product management functionality for creating and managing automation products and workflow options.

- **Hierarchy**:
    - Prominent workflow categories, filters and searchbar for easy navigation.
    - Bag and checkout options displayed prominently for convenience.


**User Flow**
1. Guest user browse the platform, explore workflow products through category filtering, sorting and detailed product pages.
2. Guest user adds products or services to the shopping bag and is redirected to required sign up or log in.
3. User creates an account or signs in to proceed with checkout.
4. Customer completes payment through Stripe, is redirected to successpage after successfull payment intent and receives an order confirmation email.
5. Customer can now access their purchases page to download purchased workflow templates securely or view their previous purchases.
6. Customer can review, update or delete their profile.
7. Superusers manage platform content through the Django admin panel. Create, update and delete automation products, workflow options and service offerings.
8. Users attempting to access invalid URLs are redirected to a custom 404 error page to help maintain navigation flow and usability.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

| Colour | Hex | Purpose | 
| --- | --- | --- | 
| Bright Snow | `#F8FAFC` | Primary background. | 
| White | `#FFFFFF` | Secondary background colour. |
| Prussian Blue | `#0F172A` | Primary text colour. |
| Blue Slate | `#475569` | Secondary text colour. |
| Royal Blue | `#2563EB` | Primary accent colour. |
| Royal Azure | `#1555E0 `| Primary hover colour. |
| Blue Spruce | `#0F766E` | Secondary accent colour. |
| Stormy Teal | `#0E6C64` | Secondary hover colour. |

![screenshot](documentation/colour-palette/E4066670-016E-40F8-B356-7EC2954E9FAD.jpeg)

This palette was chosen to communicate several important qualities:
- Trust and stability through deep blues.
- Authority and professionalism through dark text tones.
- Innovation and modern technology through teal accents.
- Clarity and accessibility through light backgrounds and strong contrast.

The combination of these colours ensures that the interface remains minimal, professional and easy to read, while also aligning with the visual language commonly used in modern technology products.


### Typography

- [Inter](https://fonts.google.com/specimen/Inter) was used as the primary font throughout the application, particularly for body text and core interface elements, due to its strong readability and clean modern appearance across desktop and mobile devices.
- [DM Sans](https://fonts.google.com/specimen/DM+Sans) was used selectively for highlighted paragraphs and supporting content to create visual contrast while maintaining the minimalist aesthetic.
- [Font Awesome](https://fontawesome.com) icons were used throughout the application for interface elements such as shopping bag actions, downloads, navigation indicators and social media links.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Sign Up | ![screenshot](documentation/wireframes/sign-up-mobile.jpeg) | ![screenshot](documentation/wireframes/sign-up-tablet.jpeg) | ![screenshot](documentation/wireframes/sign-up-desktop.jpeg) |
| Login | ![screenshot](documentation/wireframes/sign-in-mobile.jpeg) | ![screenshot](documentation/wireframes/sign-in-tablet.jpeg) | ![screenshot](documentation/wireframes/sign-in-desktop.jpeg) |
| Home | ![screenshot](documentation/wireframes/home-mobile.jpeg) | ![screenshot](documentation/wireframes/home-tablet.jpeg) | ![screenshot](documentation/wireframes/home-desktop.jpeg) |
| Workflows| ![screenshot](documentation/wireframes/workflows-mobile.jpeg) | ![screenshot](documentation/wireframes/workflows-tablet.jpeg) | ![screenshot](documentation/wireframes/workflows-desktop.jpeg) |
| Workflow detail | ![screenshot](documentation/wireframes/workflow-detail-mobile.jpeg) | ![screenshot](documentation/wireframes/workflow-detail-tablet.jpeg) | ![screenshot](documentation/wireframes/workflow-detail-desktop.jpeg) |
| Shopping bag | ![screenshot](documentation/wireframes/shopping-bag-mobile.jpeg) | ![screenshot](documentation/wireframes/shopping-bag-tablet.jpeg) | ![screenshot](documentation/wireframes/shopping-bag-desktop.jpeg) |
| Checkout | ![screenshot](documentation/wireframes/checkout-mobile.jpeg) | ![screenshot](documentation/wireframes/checkout-tablet.jpeg) | ![screenshot](documentation/wireframes/checkout-desktop.jpeg) |
| Success page | ![screenshot](documentation/wireframes/success-mobile.jpeg) | ![screenshot](documentation/wireframes/success-tablet.jpeg) | ![screenshot](documentation/wireframes/success-desktop.jpeg) |
| 404 | ![screenshot](documentation/wireframes/404-mobile.jpeg) | ![screenshot](documentation/wireframes/404-tablet.jpeg) | ![screenshot](documentation/wireframes/404-desktop.jpeg) |


## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As an anonymous user | I want to land on a clear homepage | so that I understand what the platform offers.|
| As an anonymous user | I want to browse available workflows | so that I can explore solutions before committing. |
| As an anonymous user|  I want to view workflow details | so that I understand what each automation does. |
| As an anonymous user| I want to create an account | so that I can use the websites features. |
| As a user | I want to log in securely | so that I can view my profile and purchases. |
| As a logged in user| I want to log out | so that my account remains secure. |
| As a logged in user | I want to add workflows to my bag | so that I can review before purchasing. |
| As a logged in user | I want to update or remove items from my bag | so that I stay in control of my purchase. |
| As a logged in user | I want to checkout securely | so that I can complete my purchase with confidence. |
| As a logged in user | I want to choose between workflow only, workflow & setup or custom service | so that I can decide my level of support. |
| As a logged in user | I want to download my purchased workflow | so that I can use it immediately. |
| As a logged in user | I receive a confirmation email after purchase | so that I have a backup on instructions on how to proceed. |
| As a logged in user | I can navigate to my purchase history | so that I can view all my previous purchases in one place. |
| As a logged in user | I can see a checkout confirmation | so that I can trust that the checkout process was successful. |
| As a logged in user | I can update my profile | so that my profile is always accurate. |
| As a logged in user | I want to delete my account | so that I can stay in control of my data. |


## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Sign Up | Authentication is handled through django-allauth, allowing users to securely create accounts in order to purchase workflow templates, access downloads and manage their purchase history. | ![screenshot](documentation/features/signup.jpeg) |
| Sign In | Registered users can securely log in to access their purchases and profile information. | ![screenshot](documentation/features/signin.jpeg) |
| Sign Out | Users can securely log out of their accounts to protect their purchase and profile information. | ![screenshot](documentation/features/signout.jpeg) |
| Home Page | The landing page introduces the OpsiFlow platform and guides users towards browsing products and solutions. | ![screenshot](documentation/features/home.jpeg) |
| Product Browsing | Users can browse all available automation templates and service offerings through a public product listing page with category filtering and sorting functionality. | ![screenshot](documentation/features/product-browsing.jpeg) |
| Workflow Sorting | Users can sort workflow templates and automation services by criteria such as price, complexity and alphabetical order to quickly locate suitable solutions. | ![screenshot](documentation/features/sorting.jpeg) |
| Search Functionality | A search bar allows users to quickly find products using keywords and product names. | ![screenshot](documentation/features/searchbar.jpeg) |
| Product Categories | Products are organised into categories to improve discoverability and allow users to browse relevant automation solutions more efficiently. | ![screenshot](documentation/features/categories.jpeg) |
| Product Detail Pages | Each product contains detailed information including workflow description, pricing, fulfilment options and delivery time expectations to help users choose the correct solution. | ![screenshot](documentation/features/product-details.jpeg) |
| Option Switching | Users can dynamically switch between "DIY template" and “Set Up Service” fulfilment options, as well as "Starter", "Growth" or "Pro" tier options directly within the shopping bag. | ![screenshot](documentation/features/change-option-1.jpeg) ![screenshot](documentation/features/change-option-2.jpeg) |
| Shopping Bag | Users can remove and update workflow products before checkout. | ![screenshot](documentation/features/bag-edit.jpeg) |
| Dynamic Shopping Bag Icon | The navigation shopping bag icon dynamically updates to reflect the user’s current bag total, providing immediate feedback. | ![screenshot](documentation/features/bag-icon.jpeg) |
| Offcanvas Navigation | An offcanvas navigation menu improves usability on smaller devices by providing an accessible mobile-first navigation experience. | ![screenshot](documentation/features/offcanvas.jpeg) |
| Stripe Checkout | Stripe Checkout supports multiple payment methods, providing users with a secure and flexible payment experience during checkout. | ![screenshot](documentation/features/stripe.jpeg) |
| Order Confirmation | Users receive an on-screen success page and confirmation email after successful payment completion. | ![screenshot](documentation/features/success-page.jpeg) ![screenshot](documentation/features/confirmation-email.jpeg) |
| Digital Downloads | Customers purchasing DIY workflow templates receive secure access to downloadable automation systems and setup resources. | ![screenshot](documentation/features/history-downloads.jpeg) ![screenshot](documentation/features/success-downloads.jpeg)|
| Email link to downloads | Customers recieve a link via email that provides access to their purchase history and download links after successfull log in. | ![screenshot](documentation/features/email-link.jpeg) |
| Download Limitation System | Purchased downloads are protected through a restricted download system designed to reduce unauthorised sharing and distribution. | ![screenshot](documentation/features/download-limit.jpeg) |
| Account Navigation Area | Authenticated users can access a dedicated account area for managing profile details, viewing purchases and account-related actions. | ![screenshot](documentation/features/account-nav.jpeg) |
| Purchase History | Authenticated users can access a dedicated purchases page to review previous orders and access purchased downloads. | ![screenshot](documentation/features/purchase-history.jpeg) |
| Profile Management | Users can save and manage default checkout information to improve future purchasing experiences. | ![screenshot](documentation/features/profile-management.jpeg) |
| Delete Profile Confirmation Modal | A confirmation modal is displayed before deleting a user profile to help prevent accidental destructive actions. | ![screenshot](documentation/features/delete-modal.jpeg) |
| Product Management | Superusers can create, edit and delete products, workflow options, fulfilment variations and categories through the Django admin interface. | ![screenshot](documentation/features/product-admin.jpeg) |
| Custom 404 Page | A custom 404 page was created to maintain brand consistency and guide users back into the application if an invalid URL is accessed. | ![screenshot](documentation/features/404.jpeg) |


### Future Features

- **Site Owner Dashboard**:
    - A protected staff-only dashboard displaying recent customer orders, submitted onboarding forms, contact form submissions and workflow management section.
- **Workflow Management Section**: 
    - A front-end management area where categories, products and product options can be added, updated and deleted without relying solely on the Django admin panel.
- **Onboarding Forms**:
    - User purchasing “Set Up Service” options receive onboarding forms directly via email after their purchase.
- **Automated Reminder Emails**: 
    - Automatically send reminder emails to users who have purchased setup services but have not completed their onboarding forms.
- **Newsletter System**: 
    - A newsletter feature allowing users to subscribe to updates, workflow releases and platform announcements.
- **Blog Section**: 
    - A blog section focused on automation, AI workflows, operational efficiency and productivity content.
- **Product Ratings & Reviews**: 
    - Allow customers to leave ratings and reviews on workflow templates and services to improve social proof and user trust.
- **Subscription-based Learning Platform**: 
    - Subscription access to video-based educational content, workflow tutorials and a private community area.


## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) | Online static file storage. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |
| [![MDN Web Docs](https://img.shields.io/badge/MDN%20Web%20Docs-grey?logo=mdnwebdocs&logoColor=black)](https://developer.mozilla.org/) |Tutorials/Reference Guide  |
| [![badge](https://img.shields.io/badge/favicon.io-grey?logo=fi&logoColor=209CEE)](https://favicon.io) | Generating the favicon. |
| [![badge](https://img.shields.io/badge/Google%20Fonts-grey?logo=google&logoColor=4285F4)](https://fonts.google.com/) | Typography and brand icon. |
| [![badge](https://img.shields.io/badge/Google%20Fonts-grey?logo=google&logoColor=4285F4)](https://lucid.app.com/) | Typography and icon resources used throughout the application. |
| [![YouTube](https://img.shields.io/badge/YouTube-grey?logo=youtube&logoColor=red)](https://www.youtube.com/) | Tutorials. |
| [![Medium](https://img.shields.io/badge/Medium-grey?logo=medium&logoColor=black)](https://medium.com) | Articles. |
| [![Lucid](https://img.shields.io/badge/Lucid-ERD-grey?logo=lucid&logoColor=orange)](https://lucid.app) | Planning the initial ERD |
| [![Google Sheets](https://img.shields.io/badge/Google%20Sheets-grey?logo=googlesheets&logoColor=green)](https://www.google.com/sheets/about/) | Refining the ERD |
| [![Mermaid](https://img.shields.io/badge/Mermaid-ERD-grey?logo=mermaid&logoColor=coral)](https://mermaid.live) | Creating an interactive version of the ERD |
| [![Coolors](https://img.shields.io/badge/Coolors-grey?logo=coolors&logoColor=blue)](https://coolors.co/) | Used to generate the colour palette. |
| [![Make.com](https://img.shields.io/badge/Make.com-grey?logo=make&logoColor=purple)](https://www.make.com/) | Used for workflow automation planning and business process inspiration. |
| [![Google Docs](https://img.shields.io/badge/Google%20Docs-grey?logo=googledocs&logoColor=4285F4)](https://docs.google.com/) | Text based set up guides.|
| [![Notion](https://img.shields.io/badge/Notion-grey?logo=notion&logoColor=white)](https://www.notion.so/) | Project planning, README notes and course-related study notes throughout development. |