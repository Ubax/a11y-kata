# 3.4. Focus

In this exercise, your goal is to improve how **focus** works on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/3-pitfalls/3.04-focus/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/3-pitfalls/3.04-focus/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

If you prefer not to solve the problems yourself, you can use the solution files to explore how each issue was fixed and look for any remaining problems:

- [Solution after problem 1](https://ubax.github.io/a11y-kata/3-pitfalls/3.04-focus/after-problem-1.html)
- [Solution after problem 2](https://ubax.github.io/a11y-kata/3-pitfalls/3.04-focus/after-problem-2.html)
- [Solution after all problems](https://ubax.github.io/a11y-kata/3-pitfalls/3.04-focus/after.html)


## Hints

<details>
<summary>Hint 1</summary>

Navigate in the page using the keyboard. Can you see where the focus is?

</details>

<details>
<summary>Hint 2</summary>

Navigate in the page using the keyboard. Is the focus order logical?

</details>

<details>
<summary>Hint 3</summary>

Navigate in the page using keyboard, with side menu open and closed

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

Focusable elements don’t have an outline or a visual indicator when they receive focus. This makes it hard for keyboard users to know where they are on the page. [WCAG 2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible)

</details>
<details>
<summary>Solution for problem 1</summary>

Remove `outline: none;` from the `<style>` block to ensure focus is visibly highlighted.

</details>

<details>
<summary>Problem 2</summary>

CSS is altering the visual order, but the focus follows the DOM structure, causing confusion for keyboard users. [WCAG 2.4.3 Focus Order](https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html)

</details>
<details>
<summary>Solution for problem 2</summary>

Remove the `order` property from the CSS to ensure the visual and focus order align. Learn more on [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Ordering_flex_items#the_order_property_and_accessibility).

</details>

<details>
<summary>Problem 3</summary>

When the side menu is hidden, focus can still navigate to it because it remains in the DOM.

</details>
<details>
<summary>Solution for problem 3</summary>

Two possible solutions:

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
