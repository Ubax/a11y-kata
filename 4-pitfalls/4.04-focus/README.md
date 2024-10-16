# 4.4. Focus

In this exercise, your goal is to improve how focus works on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.04-focus/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.04-focus/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

Support tool: Keyboard navigation

## Hints

<details>
<summary>Hint 1</summary>

- Navigate in the page using the keyboard and try to find where your focus is

</details>

<details>
<summary>Hint 2</summary>

- Check the order in which the focus moves through the page

</details>

<details>
<summary>Hint 3</summary>

- Navigate in the page with side menu open and closed

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

Focusable elements don’t have an outline or a visual indicator when they receive focus. This makes it hard for keyboard users to know where they are on the page.

</details>
<details>
<summary>Solution for problem 1</summary>

In the `<style>` block, remove the `outline: none;` property.

</details>

<details>
<summary>Problem 2</summary>

Visual order is modified vis CSS. The focus order follows the structure of the DOM tree. If CSS changes this order, it can confuse keyboard users.

</details>
<details>
<summary>Solution for problem 2</summary>

Remove the `order` property from the CSS. Using the `order` property can cause the visual order to not match the logical order, making navigation harder. Learn more on [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Ordering_flex_items#the_order_property_and_accessibility).

</details>

<details>
<summary>Problem 3</summary>

When the side menu is hidden, the focus can still go there because it’s still part of the DOM tree.

</details>
<details>
<summary>Solution for problem 3</summary>

Here are two possible solutions:

1. Using the [`inert`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inert) attribute
   ```js
   hamburger.addEventListener("click", () => {
       ...
       sideMenu.inert = !sideMenu.classList.contains("active");
   });
   ```
2. Use `display: none` instead of moving the menu off-screen with `left: -...`. Note that this will disable the animation.
   ```css
   .side-menu {
       ...
       display: none;
   }
   .side-menu.active {
       display: block;
   }
   ```

</details>

## Resources

- [WCAG 2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible)
- [WCAG 2.4.3 Focus Order](https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html)
- [Accessibility of CSS order - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/order#accessibility)
- [`intert`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inert)
