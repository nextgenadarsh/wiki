Angular Interview Questions
---

## AngularJs vs Angular

Feature | AngularJS | Angular
-- | -- | --
Architecture | Supports MVC design Model | Angular uses components and directives
Language | AngularJS uses javascript | Angular using TypeScript
Syntax | AngularJS uses ng directive to bind images, property and events | Angular uses [] to bind property and () to bind events
Mobile Supports | AngularJS does not provide mobile support | Angular provides mobile support 
Dependency Injection | AngularJS doesn't support the concept of dependency injection | Angular supports the concept of dependency injection with change detection
Routing | In AngularJS $routeprovider.when() is used for routing configs | RouteConfig{()} is used for routing configs
Structure | less manageable for large applications | makes development and maintenance of large applications easier
Speed | less faster | faster than AngularJS 

## Advantage of Angular

- Mobile supports
- Supports two way data binding
- MVC architecture
- Supports RESTfull services
- Supports dependency injections
- Custom directives
- Supports Validation feature

## MVVM Architecture

- MVC Architecture separates an application into three main logical components Model, View and Controlller.
- Model encapsulates data and business logic. This can includes data retrived from APIs, user inputs and application state
- The View defines the UI of the application that is HTML templates
- Controller focusing on managing data flow and business logic

## Modules

- Angular modules are logical groups of components, directives, pipes and services. 
- An angular application needs at least one module as root module but can have more modules.

## Services
Services are used to organise and share code across the application 

## Service vs Factory

## Controllers

## Nested Controller

## Directives

- Element directives − Directive activates when a matching element is encountered.
- Attribute − Directive activates when a matching attribute is encountered.
- CSS − Directive activates when a matching CSS style is encountered.
- Comment − Directive activates when a matching comment is encountered

## Component and Directive Lifecycle

## Decorators

## Templates

## Provider

## scope vs $scope

## Scope Hierarchy

## Data Binding

## Expressions

## Filters

- currency: Format a number to a currency format.
- date: Format a date to a specified format.
- filter: Select a subset of items from an array.
- json: Format an object to a JSON string.
- limit: To Limits an array/string, into a specified number of elements/characters.
- lowercase: Format a string to lower case.
- number: Format a number to a string.
- orderBy: Orders an array by an expression.
- uppercase: Format a string to upper case.

## Annotation vs Decorator?

## String Interpolation?

## Data Sharing between Components

- Data Sharing Between Angular Components
- Parent to Child: via Input
- Child to Parent: via Output() and EventEmitter
- Child to Parent: via ViewChild
- Unrelated Components: via a Service

## Communicate between Modules

- Using events
- Using services
- By assigning models on $rootScope
- Directly between controllers [$parent, $$childHead, $$nextSibling, etc.]
- Directly between controllers [ControllerAs, or other forms of inheritance]

## Eager vs Lazy Loading

## Template based vs Reactive Forms

## Angular Ahead-of-Time (AOT) compiler

## jQLite

## Digest Cycle

## Dependency Injection

## One Way vs Two Way Binding

## Dirty Checking

