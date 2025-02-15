

xyz.wagyourtail.jsmacros.core.service.ServiceManager
----------------------------------------------------

#### 

1.6.3

### Constructors

#### new ServiceManager (runner)

| Parameter | Type | Description |
|---|---|---|
| runner | Core<?, ?> |  |



#### Methods

[registerService(name, pathToFile)](#registerService-String-String-)


[registerService(name, pathToFile, enabled)](#registerService-String-String-boolean-)


[registerService(name, trigger)](#registerService-String-ServiceTrigger-)


[unregisterService(name)](#unregisterService-String-)


[disableReload(serviceName)](#disableReload-String-)


[renameService(oldName, newName)](#renameService-String-String-)


[getServices()](#getServices-)


[startService(name)](#startService-String-)


[stopService(name)](#stopService-String-)


[setAutoUnregisterKeepAlive(ctx, keepAlive)](#setAutoUnregisterKeepAlive-BaseScriptContext-boolean-)
S


[hasKeepAlive(ctx)](#hasKeepAlive-BaseScriptContext-)
S


[restartService(name)](#restartService-String-)


[enableService(name)](#enableService-String-)


[disableService(name)](#disableService-String-)


[isRunning(name)](#isRunning-String-)


[isEnabled(name)](#isEnabled-String-)


[status(name)](#status-String-)


[getServiceData(name)](#getServiceData-String-)


[getTrigger(name)](#getTrigger-String-)


[load()](#load-)


[save()](#save-)


[stopReloadListener()](#stopReloadListener-)


[startReloadListener()](#startReloadListener-)


[markCrashed(serviceName)](#markCrashed-String-)


[isCrashed(serviceName)](#isCrashed-String-)


[tickReloadListener()](#tickReloadListener-)



### Methods

#### .registerService(name, pathToFile)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| pathToFile | String | relative to macro folder |

##### Returns: boolean

false if service with that name is already registered



#### .registerService(name, pathToFile, enabled)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| pathToFile | String | relative to macro folder |
| enabled | boolean |  |

##### Returns: boolean

false if service with that name is already registered



#### .registerService(name, trigger)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |
| trigger | ServiceTrigger |  |

##### Returns: boolean

false if service with that name already registered



#### .unregisterService(name)

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: boolean



#### .disableReload(serviceName)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| serviceName | String | the name of the service to disable the reload feature for |

##### Returns: void



#### .renameService(oldName, newName)

| Parameter | Type | Description |
|---|---|---|
| oldName | String |  |
| newName | String |  |

##### Returns: boolean

false if service with new name already registered or old name doesn't exist



#### .getServices()


##### Returns: [Set](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)>

registered service names



#### .startService(name)

starts service once

| Parameter | Type | Description |
|---|---|---|
| name | String | service name |

##### Returns: [ServiceManager$ServiceStatus](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html)

previous state (or [ServiceManager$ServiceStatus#UNKNOWN](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#UNKNOWN) if unknown service)



#### .stopService(name)

| Parameter | Type | Description |
|---|---|---|
| name | String | service name |

##### Returns: [ServiceManager$ServiceStatus](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html)

previous state (or [ServiceManager$ServiceStatus#UNKNOWN](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#UNKNOWN) if unknown service)



#### .setAutoUnregisterKeepAlive(ctx, keepAlive)

Static
| Parameter | Type | Description |
|---|---|---|
| ctx | BaseScriptContext<?> |  |
| keepAlive | boolean |  |

##### Returns: void



#### .hasKeepAlive(ctx)

Static
| Parameter | Type | Description |
|---|---|---|
| ctx | BaseScriptContext<?> |  |

##### Returns: boolean



#### .restartService(name)

| Parameter | Type | Description |
|---|---|---|
| name | String | service name |

##### Returns: [ServiceManager$ServiceStatus](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html)

state before "restarting" (or [ServiceManager$ServiceStatus#UNKNOWN](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#UNKNOWN) if unknown service)



#### .enableService(name)

| Parameter | Type | Description |
|---|---|---|
| name | String | service name |

##### Returns: [ServiceManager$ServiceStatus](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html)

previous state (or [ServiceManager$ServiceStatus#UNKNOWN](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#UNKNOWN) if unknown service)



#### .disableService(name)

| Parameter | Type | Description |
|---|---|---|
| name | String | service name |

##### Returns: [ServiceManager$ServiceStatus](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html)

previous state (or [ServiceManager$ServiceStatus#UNKNOWN](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#UNKNOWN) if unknown service)



#### .isRunning(name)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| name | String | the name of the service to check |

##### Returns: boolean

`true` if the service is running, `false` otherwise.



#### .isEnabled(name)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| name | String | the name of the service to check |

##### Returns: boolean

`true` if the service is enabled, `false` otherwise.



#### .status(name)

| Parameter | Type | Description |
|---|---|---|
| name | String | service name |

##### Returns: [ServiceManager$ServiceStatus](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html)

[ServiceManager$ServiceStatus#UNKNOWN](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#UNKNOWN) if unknown service, [ServiceManager$ServiceStatus#RUNNING](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#RUNNING) if disabled and running, [ServiceManager$ServiceStatus#DISABLED](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#DISABLED) if disabled and stopped, [ServiceManager$ServiceStatus#STOPPED](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#STOPPED) if enabled and stopped, [ServiceManager$ServiceStatus#ENABLED](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceManager.ServiceStatus.html#ENABLED) if enabled and running.



#### .getServiceData(name)

1.6.5

this might throw if the service is not running...

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [EventService](1.9.2/xyz/wagyourtail/jsmacros/core/service/EventService.html)

the event that is current for the service



#### .getTrigger(name)

1.6.5 [named getServiceData previously]

| Parameter | Type | Description |
|---|---|---|
| name | String |  |

##### Returns: [ServiceTrigger](1.9.2/xyz/wagyourtail/jsmacros/core/service/ServiceTrigger.html)



#### .load()

load services from config


##### Returns: void



#### .save()

save current registered services & enabled/disabled status to config


##### Returns: void



#### .stopReloadListener()

1.8.4

Stops the service manager from reloading scrips on file changes.


##### Returns: void



#### .startReloadListener()

1.8.4

Will make the service manager reload scripts on file changes.


##### Returns: void



#### .markCrashed(serviceName)

1.8.4

Mark a service as crashed so that it can be reloaded when its file changes. Crashed services
must be marked so that file change listener knows to restart them even if they are not
running because they crashed.

| Parameter | Type | Description |
|---|---|---|
| serviceName | String | the name of the service to mark as crashed |

##### Returns: void



#### .isCrashed(serviceName)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| serviceName | String | the name of the service to check |

##### Returns: boolean

`true` if the service previously crashed, `false` otherwise.



#### .tickReloadListener()

1.8.4

Ticks the service manager. This will check if any services need to be reloaded and reloads
them if necessary.


##### Returns: void




