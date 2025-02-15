

xyz.wagyourtail.jsmacros.core.library.impl.FFS
----------------------------------------------

#### extends [PerExecLibrary](1.9.2/xyz/wagyourtail/jsmacros/core/library/PerExecLibrary.html)

1.1.8

Better File-System functions.

An instance of this class is passed to scripts as the `FS` variable.

#### Methods

[list(path)](#list-String-)


[exists(path)](#exists-String-)


[isDir(path)](#isDir-String-)


[isFile(path)](#isFile-String-)


[getName(path)](#getName-String-)


[toRelativePath(absolutePath)](#toRelativePath-String-)


[createFile(path, name)](#createFile-String-String-)


[createFile(path, name, createDirs)](#createFile-String-String-boolean-)


[makeDir(path)](#makeDir-String-)


[move(from, to)](#move-String-String-)


[copy(from, to)](#copy-String-String-)


[unlink(path)](#unlink-String-)


[combine(patha, pathb)](#combine-String-String-)


[getDir(path)](#getDir-String-)


[open(path)](#open-String-)


[open(path, charset)](#open-String-String-)


[walkFiles(path, maxDepth, followLinks, visitor)](#walkFiles-String-int-boolean-MethodWrapper-)


[toRawFile(path)](#toRawFile-String-)


[toRawPath(path)](#toRawPath-String-)


[getRawAttributes(path)](#getRawAttributes-String-)



### Methods

#### .list(path)

1.1.8

List files in path.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)[]

An array of file names as [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html).



#### .exists(path)

1.1.8

Check if a file exists.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: boolean



#### .isDir(path)

1.1.8

Check if a file is a directory.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: boolean



#### .isFile(path)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| path | String | the path relative to the script's folder |

##### Returns: boolean

`true` if the path leads to a file, `false` otherwise.



#### .getName(path)

1.1.8

Get the last part (name) of a file.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

a [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) of the file name.



#### .toRelativePath(absolutePath)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| absolutePath | String | the absolute path to the file |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

a path relative to the script's folder to the given absolute path.



#### .createFile(path, name)

1.8.4

Creates a new file in the specified path, relative to the script's folder. This will only
work if the parent directory already exists. See [FFS#createFile(java.lang.String,java.lang.String,boolean)](#createFile-String-String-boolean-)
to automatically create all parent directories.

| Parameter | Type | Description |
|---|---|---|
| path | String | the path relative to the script's folder |
| name | String | the name of the file |

##### Returns: boolean

`true` if the file was created successfully, `false` otherwise.



#### .createFile(path, name, createDirs)

1.8.4

Creates a new file in the specified path, relative to the script's folder. Optionally parent
directories can be created if they do not exist.

| Parameter | Type | Description |
|---|---|---|
| path | String | the path relative to the script's folder |
| name | String | the name of the file |
| createDirs | boolean | whether to create parent directories if they do not exist or not |

##### Returns: boolean

`true` if the file was created successfully, `false` otherwise.



#### .makeDir(path)

1.1.8

Make a directory.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: boolean

a [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html) for success.



#### .move(from, to)

1.1.8

Move a file.

| Parameter | Type | Description |
|---|---|---|
| from | String | relative to the script's folder. |
| to | String | relative to the script's folder. |

##### Returns: void



#### .copy(from, to)

1.1.8

Copy a file.

| Parameter | Type | Description |
|---|---|---|
| from | String | relative to the script's folder. |
| to | String | relative to the script's folder. |

##### Returns: void



#### .unlink(path)

1.2.9

Delete a file.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: boolean

a [Boolean](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/Boolean.html) for success.



#### .combine(patha, pathb)

1.1.8

Combine 2 paths.

| Parameter | Type | Description |
|---|---|---|
| patha | String | path is relative to the script's folder. |
| pathb | String |  |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

a [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) of the combined path.



#### .getDir(path)

1.1.8

Gets the directory part of a file path, or the parent directory of a folder.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html)

a [String](https://docs.oracle.com/javase/8/docs/api/index.html?java/lang/String.html) of the combined path.



#### .open(path)

1.1.8

Open a FileHandler for the file at the specified path.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |

##### Returns: [FileHandler](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/FileHandler.html)

a [FileHandler](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/FileHandler.html) for the file path.



#### .open(path, charset)

1.8.4

Open a FileHandler for the file at the specified path.

| Parameter | Type | Description |
|---|---|---|
| path | String | relative to the script's folder. |
| charset | String | the charset to use for reading/writing the file (default is UTF-8) |

##### Returns: [FileHandler](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/FileHandler.html)

a [FileHandler](1.9.2/xyz/wagyourtail/jsmacros/core/library/impl/classes/FileHandler.html) for the file path.



#### .walkFiles(path, maxDepth, followLinks, visitor)

1.8.4

An advanced method to walk a directory tree and get some information about the files, as well
as their paths.

| Parameter | Type | Description |
|---|---|---|
| path | String | the relative path of the directory to walk through |
| maxDepth | int | the maximum depth to follow, can cause stack overflow if too high |
| followLinks | boolean | whether to follow symbolic links |
| visitor | MethodWrapper<String, BasicFileAttributes, ?, ?> | the visitor that is called for each file with the path of the file and its
                                            attributes |

##### Returns: void



#### .toRawFile(path)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| path | String | the relative path to get the file object for |

##### Returns: [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html)

the file object for the specified path.



#### .toRawPath(path)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| path | String | the relative path to get the path object for |

##### Returns: [Path](https://docs.oracle.com/javase/8/docs/api/index.html?java/nio/file/Path.html)

the path object for the specified path.



#### .getRawAttributes(path)

1.8.4

| Parameter | Type | Description |
|---|---|---|
| path | String | the path relative to the script's folder |

##### Returns: [BasicFileAttributes](https://docs.oracle.com/javase/8/docs/api/index.html?java/nio/file/attribute/BasicFileAttributes.html)

the attributes of the file at the specified path.




