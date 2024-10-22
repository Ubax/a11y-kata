# 3.3. Links

In this exercise, your task is to improve the accessibility of the **links** on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/3-pitfalls/3.03-links/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/3-pitfalls/3.03-links/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

If you prefer not to solve the problems yourself, you can use the solution files to explore how each issue was fixed and look for any remaining problems:

- [Solution after problem 1](https://ubax.github.io/a11y-kata/3-pitfalls/3.03-links/after-problem-1.html)
- [Solution after all problems](https://ubax.github.io/a11y-kata/3-pitfalls/3.03-links/after.html)

## Hints

<details>
<summary>Hint 1</summary>

Disable colors in your browser and try to identify the links.

Refer to [2.5 Disability simulation - Color blindness](../../2-tools/2.5-disability-simulation.md#exercise-1-simulating-color-blindness) for instructions on how to disable colors in the browser.

</details>

<details>
<summary>Hint 2</summary>

Use a screen reader to navigate through the links. Can you tell what each link does?

- Mac: <kbd>Ctrl + Option + Cmd + L</kbd>
- Windows: <kbd>K</kbd>
- Android: <kbd>Swipe up + down</kbd> to select links, then <kbd>Swipe down</kbd>
- iOS: <kbd>Twist</kbd> to select links, then <kbd>Swipe down</kbd>

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

Links are only highlighted by color, making it hard for users with color blindness to distinguish them from the surrounding text. [WCAG Failure 73](https://www.w3.org/WAI/WCAG21/Techniques/failures/F73)

</details>
<details>
<summary>Solution for problem 1</summary>

Remove `style="text-decoration: none; cursor: default"` from the links. Use a non-color visual cue, like underlining, to indicate links.

</details>

<details>
<summary>Problem 2</summary>

For users relying on screen readers or speech recognition, non-descriptive link text such as "Read more" doesn’t convey the purpose of the link, making navigation difficult. [WCAG 2.4.4](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context), [WCAG 2.4.9](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-link-only).

</details>
<details>
<summary>Solution for problem 2</summary>

There are a few ways to fix this:

- Change the link text to be more descriptive, e.g., "Read more about the rise of the internet" instead of just "Read more."
- Add an `aria-label` to provide extra context, like `<a href="..." aria-label="Read more about the rise of the internet">Read more</a>`.
- Wrap the post title in a link and add `aria-hidden="true"` to the "Read more" link, e.g., `<a ...><h2 class="post-title">The Evolution of the Keyboard</h2></a>`.

You can find examples in the [after.html](./after.html) file.

</details>

## Resources

- [WCAG 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color)
- [WCAG 2.4.4 Link Purpose (In Context)](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context)
- [WCAG 2.4.9 Link Purpose (Link Only)](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-link-only)
- [How to use aria-label on link](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA8)
- [Providing descriptive link text](https://www.w3.org/WAI/WCAG21/Techniques/general/G91)
- [`<a>` tag docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
