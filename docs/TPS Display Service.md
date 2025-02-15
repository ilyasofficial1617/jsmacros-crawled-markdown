

TPS Display Service
-------------------

example code for a service that displays the tps in an overlay in the bottom
left corner of the screen.
  

  

To register a service, select service tab on the top bar.
(or click the service button in the bottom left next to "running" if you're on older version of jsmacros)
Give it a name, and assign a file. the enable/disable will determine if the service should start at startup,
you can manully start/stop with the run/stop button.

```

// services start with minecraft, when enabled and are meant to be persistent scripts.
JsMacros.assertEvent(event, "Service");

const d2d = Hud.createDraw2D();
let tpsmeter = null;

d2d.setOnInit(JavaWrapper.methodToJava(() => {
    tpsmeter = d2d.addText(World.getServerTPS(), 0, d2d.getHeight() - 10, 0xFFFFFF, true);
}));

const tickListener = JsMacros.on("Tick", JavaWrapper.methodToJava(() => {
    tpsmeter?.setText(World.getServerTPS());
}));

d2d.register();

// this fires when the service is stopped
event.stopListener = JavaWrapper.methodToJava(() => {
    d2d.unregister();
    JsMacros.off(tickListener);
});
  
  
```
