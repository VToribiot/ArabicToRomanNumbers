# Requirements, Criteria and Cases
___


### ¿Qué es un Coding Dojo? referencia https://lorenzosolano.com/what-is-coding-dojo/

A Coding Dojo is a meeting where a bunch of coders gathers around to work on a programming challenge. Programmers of different skill levels are invited to engage to practice and collaborate as equals.
	
The goal is to learn, teach and improve with fellow software developers in a non-competitive environment.

The premise of a Coding Dojo is to promote continuous learning in a safe space. It is both non-competitive and inclusive.

### Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia. Referencia https://lorenzosolano.com/requirements-acceptance-criteria-and/

* Requirements are properties that must be executed or have to achieve the product's intended purpose.
* Acceptance Criteria are the set of parameters used to evaluate a specific aspect of the stage of the project. The level of acceptance is directly proportional to the number of parameters that achieves correctly.
* A testing Scenario is a contextual framework in which an acceptance criterion is created or validated.

	The difference between the last two aspects is that they serve to evaluate and check the correctness of the previous aspect to guarantee its functionality and evolution throughout the lifecycle of the software. Meanwhile, the requirements are the expectations and need to be fulfilled and continuously revised.

	An example of this is when you want to create a paper plane, and you, firstly, that flies very far away; that's a requirement. To execute this, you establish that it needs large wings and an aerodynamic design; these are the acceptance criteria. Lastly, these criteria are only valuable when it isn't windy or isn't raining either; these are the testing scenario.

### Dé dos ejemplos de requerimientos no-funcionales, y especifique cual es su categoría (seguridad, performance, portabilidad, etc.)

An example of a non-functional requirement in a program is its ability to be executed in several environments; this is a portability requirement. Uber, Opera, and Notion are some examples of multi-platform applications.

Another example is when an application is always ready to use whenever the right conditions exists; this is an availability requirement. Google, Whatsapp, Instagram and many more applications have a structure around it's capacity to be accesible to the public at anytime.	

### ¿Qué es TDD?

Test driven development (TDD) is a software development approach in which a test is written before writing the code. The test is done before testing the functionality and ensures that the application is suitable for testability.

In other terms, test cases for each functionality are created and tested first. If the test fails, the new code is built to pass the test, making simple and efective code.

### ¿Que son pruebas unitarias automatizadas?

Unit tests are tiny pieces of code that developers write, execute, and maintain. These tests exercise the code at level that it wouldn't usually be interesting or understandable to non-developers. It prevents regression defects and gives software developers confidence in changing the code without damaging any related parts. 

The goal of automated unit testing is to demonstrate that each part of software works as intended, also may also aid in documenting the software's functionality while significantly speeding up the feedback loop on defect detection.

### ¿Cual fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?

The first unit testing framework framework was JUnit created back in 1997, by a programmer called Kent Beck for JavaScript. This tool started as a development environment plugin to test small pieces of code. Developers wrote test code that assessed the source code, marking the beginning of unit testing. 

### ¿Describa los componentes de la arquitectura xUnit?

The xUnits all have the same basic architecture. The key classes are TestCase, TestRunner, TestFixture, TestSuite, and TestResult.
	
+ Test Case: it's the base class for a unit test; all of them are inherited from it. To create a unit test, define a test class that's descended from TestCase and add a test method to it.
+ Test Runner: reports details about the test results and simplifies the test. Their purpose is to run one or more TestCases and report the results. There are 3 variants of this element named: AWT Test Runner, Swing Test Runner, and Textual Test Runner.
+ Test Fixture: a group of preconditions or states needed to run a test. Every TestCase is implicitly a TestFixture, although it may not act like one. The TestFixture behavior comes into play when multiple test methods have objects in common.
+ Test Suite: a class for aggregating unit tests closely related to TestCase, since both are descendants of the same abstract class.
+ Test Result: Each time a test is executed, the TestResult object is passed in to collect the results. The immediate goal of running unit tests is to accumulate test results.

![](../Downloads/utf_0306.gif)

### Indique al menos tres desventajas de las pruebas unitarias automatizadas

Some disadvantages of automated unit testing are:
* Is very much more expensive than manual testing.
* May require additionally trained and skilled people.
* Only removes the mechanical execution of the testing process, but the creation of test cases still requires testing professionals.

### Indique al menos tres ventajas de las pruebas unitarias automatizadas

Some advantages of automated unit testing are:
* Is faster than manual execution.
* Reduces the dependability of test engineers.
* Takes fewer resources in execution compared to manual testing.
* Has fewer chances of error hence more reliable.

### Tomando el algoritmo de conversión de números arábigos o "decimales" a números Romanos:

  * **Cree un documento donde se listen los Requerimientos, Criterios de Aceptación y Casos de Prueba para una aplicación de consola**

  * **Los casos de prueba deben ser de dos categorías: End-To-End** (desde el UI) **y Unitarios** (caja blanca, código, bajo nivel)

### Utilizando el lenguaje de su preferencia cree cinco o más casos de prueba unitarios automatizados utilizando un framework de automatización de pruebas para el algoritmo en cuestión





















