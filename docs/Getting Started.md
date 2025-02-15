

Getting Started
---------------

### Download

[Curseforge](https://curseforge.com/minecraft/mc-mods/jsmacros) [(Mirror)](https://github.com/wagyourtail/JsMacros)
### About

  

If you are not satisfied with the internal editor, some good editors are [VS Code](https://code.visualstudio.com/),
[Notepad++](https://notepad-plus-plus.org/)
and [Sublime](https://www.sublimetext.com/), or you can join the [Discord](https://discord.gg/P6W58J8) and give me suggestions.
  

  
### Info

I set it to be multi-threaded so that multiple scripts could run at once. This also prevents the game from crashing if you accidentally make a forever loop.
Functions can't be passed between scripts, some variables *can* but only if they're converted to java variables first... look at [the Graal JavaScript Compatibility Docs](https://github.com/graalvm/graaljs/blob/master/docs/user/JavaScriptCompatibility.md)) for some raw java stuff you can do.
  

  

In the JS Compatibility docs, you may have noticed `Java.type` to directly grab java classes... to easier facilitate this I have created a [Minecraft Mapping Viewer](1.9.2/https://wagyourtail.xyz/Projects/MinecraftMappingViewer/App) so you will be able to figure out the obfuscated (for fabric this is Yarn Intermediary) names of the Minecraft classes/methods/functions you wish to use.
Some classes may not work with `Java.type` in which case you can look at the [Reflection library](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/FReflection.html).
  

  

you can find some reference on the difference between the JS embedded in Java and Node.js specifications [here](https://www.graalvm.org/reference-manual/js/NodeJSvsJavaScriptContext/).
mainly:
JavaScript code embedded in a Java application has access to limited capabilities, as specified through the Context API, and do not have access to Node.js built-in modules.

You can work around some of this, however. either by using java alternatives or finding pure js versions of them.
  

  

Feel free to join the [Discord](https://discord.gg/P6W58J8) and ask any questions.
  

  
### Acknolegements

[![JProfiler](https://www.ej-technologies.com/images/product_banners/jprofiler_small.png)
Thank You to JProfiler for usage of the Java Profiler tool for optimizing jsmacros!](https://www.ej-technologies.com/products/jprofiler/overview.html)