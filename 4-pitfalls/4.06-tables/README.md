# 4.6. Tables

In this exercise, your goal is to improve the accessibility of the **table** on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.06-tables/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.06-tables/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

## Hints

<details>
<summary>Hint - How to use a screen reader with tables</summary>

- To locate tables:
  - macOS: <kbd>VO + Command + T</kbd>
  - Windows: <kbd>Control + Alt + T</kbd>
  - Alternatively on macOS use <kbd>VO + U</kbd> to open the rotor, then navigate with the arrow keys to find tables.
- To read tables:
  - Use <kbd>VO + Arrows</kbd> (macOS) or <kbd>Control + Alt + Arrows</kbd> (Windows) to move through cells.
  - Use <kbd>VO + C</kbd> or <kbd>Control + Alt + C</kbd> to read the current column header.
  - Use <kbd>VO + R</kbd> or <kbd>Control + Alt + R</kbd> to read the current row header.

</details>

<details>
<summary>Hint 1</summary>

Using a screen reader, find the exchange rate for the British Pound (GBP) on October 2, 2024.

</details>

<details>
<summary>Hint 2</summary>

Did the screen reader announce the date?

</details>

<details>
<summary>Hint 3</summary>

Did the screen reader announce the currency name or abbreviation?

</details>

<details>
<summary>Hint 4</summary>

When entering the table, did the screen reader announce the table's name?

</details>

## Problems & Solutions

<details>
<summary>Problem 1</summary>

The table lacks column headers, making it difficult for screen reader users to understand which data belongs to which column.

</details>
<details>
<summary>Solution for Problem 1</summary>

Use `<th>` tags with `scope="col"` to define column headers.

```diff
<tr>
-  <td rowspan="2">Currency</td>
+  <th scope="col" rowspan="2">Currency</th>
-  <td colspan="5">October 2024</td>
+  <th scope="colgroup" colspan="5">October 2024</th>
-  <td colspan="2">September 2024</td>
+  <th scope="colgroup" colspan="2">September 2024</th>
</tr>
<tr>
-  <td>7th</td>
+  <th scope="col">7th</th>
  ...
-  <td>27th</td>
+  <th scope="col">27th</th>
</tr>
```

</details>

<details>
<summary>Problem 2</summary>

The table lacks row headers, making it hard for screen reader users to understand which data belongs to which row.

</details>
<details>
<summary>Solution for Problem 2</summary>

Use `<th>` tags with `scope="row"` to define row headers.

```diff
<tr>
-  <td>USD</td>
+  <th scope="row">USD</th>
  <td>1.0982</td>
  ...
  <td>1.1158</td>
</tr>
...
```

</details>

<details>
<summary>Problem 3</summary>

The table lacks a caption, which helps screen reader users identify and understand the table's purpose.

</details>
<details>
<summary>Solution for Problem 3</summary>

Add a caption by using one of the following:

- `aria-labelledby` to reference a caption element.
  ```diff
  - <h2>Currency Exchange Rates for Euro</h2>
  + <h2 id="currency-exchange-rate">Currency Exchange Rates for Euro</h2>
  - <table>
  + <table aria-labelledby="currency-exchange-rate">
    ...
  </table>
  ```
- `<caption>` element to label the table.
  ```diff
  - <h2>Currency Exchange Rates for Euro</h2>
  <table>
  +  <caption>
  +    <h2>Currency Exchange Rates for Euro</h2>
  +  </caption>
    ...
  </table>
  ```

</details>

## Resources

- [W3C Tables Tutorial](https://www.w3.org/WAI/tutorials/tables/)
- [WCAG 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships)
- [Creating Accessible Tables - WebAIM](https://webaim.org/techniques/tables/data)
- [`<table>` Element Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
