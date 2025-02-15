

Extensions
----------

Language Extensions
-------------------

These extensions allow you to code in languages other than JavaScript, and some even have performance benefits.

* Jython (python 2.7 support) - [Github Download](https://github.com/JsMacros/JsMacros-Jython/releases)
* JEP (python 3.x support) - [Github Download](https://github.com/JsMacros/JsMacros-JEP/releases)
* Lua (lua 5.2 support) - [Github Download](https://github.com/JsMacros/JsMacros-Lua/releases)
* Ruby (Ruby 2.6.x support) - [Github Download](https://github.com/JsMacros/JsMacros-Ruby/releases)
* Groovy (Groovy 4.0.4 support) - [Github Download](https://github.com/JsMacros/JsMacros-Groovy/releases)
* Kotlin (Kotlin 1.7.10 support) - [Github Download](https://github.com/JsMacros/JsMacros-Kotlin/releases)
* WASM/WASI (WasmTime 0.11.0 support) - [Github Download](https://github.com/JsMacros/JsMacros-WASM/releases)

### Installation

To install jsmacros extensions, place the jar files in the `.minecraft/config/jsMacros/LanguageExtensions/` folder.

Benchmarks
----------

![Everything's faster than JavaScript, except wasm/groovy interop](img/updated_bm.png)
  

  

Jython, Lua and Ruby will have a good performance benefit for most tasks.
  

*Plus, their threading scheme for launguage contexts works better,
so you can have true async.*
  

  

JEP/Groovy's good until you try to access a lot of different Java objects.
  

*but jep can be a pain to install, and has threading concerns like js*
  

  

Kotlin is faster, but is more strongly typed and null-checked, so it may be harder to write valid scripts in.
  

  

WASM/WASI is a joke.
  

*have you seen its java interop code.*
### Debugging

for debugger attaching in js, see [JsMacros Debugging](https://github.com/JsMacros/JsMacros-Debugging)
