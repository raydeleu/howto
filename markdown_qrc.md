# Quick Reference for Markdown

## Headers

    #    header 1
    ##   header 2
    ###  header 3
 
## Emphasis 

    *This text will be italic*
    _This will also be italic_

    **This text will be bold**
    __This will also be bold__

    _You **can** combine them_

## Lists

### Unordered

```
  * apples
     * (indented three spaces) red apples
     * green apples 
  * oranges
  * pears
```

* apples
   * (indented three spaces) red apples
   * green apples 
* oranges
* pears
 
### Ordered
```
1. apples
   1. (indented three spaces) red apples
   1. green apples
1. oranges
1. pears
```

1. apples
   1. (indented three spaces) red apples
   1. green apples
1. oranges
1. pears

## Images

```
![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png){width=500} 
width works only in PanDoc, not on GitHub. 

<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="drawing" width="100"/>
```

<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="drawing" width="100"/>

## Code

```
Indent 4 spaces or use three ```  before and after the code

with ```javascript you can add syntax highlighting

```

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```
## Inline code
```
I think you should use an
`<addr>` element here instead.
```

I think you should use an
`<addr>` element here instead.

## Task Lists

```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
```

If you include a task list in the first comment of an Issue, you will get a handy progress indicator in your issue list. It also works in Pull Requests!

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

## Tables
You can create tables by assembling a list of words and dividing them with hyphens - (for the first row), and then separating each column with a pipe |:
```
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

```
Would become:

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column




## Blockquotes
As Kanye West said:
```
> We're living the future so
> the present is our past.
```

> We're living the future so
> the present is our past.

## Username @mentions
Typing an @ symbol, followed by a username, will notify that person to come and view the comment. This is called an “@mention”, because you’re mentioning the individual. You can also @mention teams within an organization.
