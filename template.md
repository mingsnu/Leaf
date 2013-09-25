# Leaf Example

## Code highlight

```html
<link rel="stylesheet" href="styles/default.css">
<script src="highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
```

 ```javascript
 var s = "JavaScript syntax highlighting";
 alert(s);
 ```
 
 ```python
 s = "Python syntax highlighting"
 print s
 ```

```r
x=1:10
y=x+nrom(10)
plot(x)
abline(lm(y~x))
```
 
 ```
 No language indicated, so no syntax highlighting. 
 But let's throw in a <b>tag</b>.
 ```

## List test

- First
- Second
- Third


## Table Test

### Using html syntax

<table>
  <tr>
    <th>ID</th><th>Name</th><th>Rank</th>
  </tr>
  <tr>
    <td>1</td><td>Tom Preston-Werner</td><td>Awesome</td>
  </tr>
  <tr>
    <td>2</td><td>Albert Einstein</td><td>Nearly as awesome</td>
  </tr>
</table>


### EXT_TABLES — Parse [PHP-Markdown tables](http://michelf.ca/projects/php-markdown/extra/#table)

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

### Quote

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 

### Reference

1. [MMarkdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
2. [Misaka](http://misaka.61924.nl)
3. [Houdini.py](http://python-houdini.61924.nl/)
4. [Pygments](http://pygments.org/)

### TODO:

1. Highlight *no language* code
2. Modify the css file

