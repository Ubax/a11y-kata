# 4.3. Links

In this exercise, your task is to enhance the accessibility of the links on page [before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.03-links/before.html) ([code source](./before.html)).

Additionally, you can refer to the [after.html](after.html) file to compare your solutions.

Support tools: 
- Color simulator
- Screen reader

## Hints

<details>
<summary>Hint 1</summary>

- Try finding the links with colors disabled

</details>

<details>
<summary>Hint 2</summary>

- Using screen reader try to find the purpose of the links

TODO: Maybe use rotor to find correct link

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

The first issue is that links are only highlighted by color. This can pose challenges for users with color blindness or low vision, as they may struggle to distinguish the links from the surrounding text.

</details>
<details>
<summary>Solution for problem 1</summary>

Remove `style="text-decoration: none; cursor: default"` from the links. It’s essential to provide a non-color visual indicator for links, such as underlining or changing the text style.

</details>

<details>
<summary>Problem 2</summary>

When users rely on screen readers or speech recognition software, they may not understand the purpose of a link if the link text is not descriptive. This lack of clarity makes it difficult for these users to navigate effectively.

</details>
<details>
<summary>Solution for problem XX</summary>

There are several ways to address this issue:

- Change the link text to be more descriptive, such as using "Read more about the rise of the internet" instead of just "Read more."
- Use the `aria-label` attribute to provide a more descriptive label for the link, for example: `<a href="..." aria-label="Read more about the rise of the internet">Read more</a>`.
- Wrap the post title in a link and add an `aria-hidden="true"` attribute to the "Read more" link, like this: `<a ...><h2 class="post-title">The Evolution of the Keyboard</h2></a>`.

You can see examples of each solution in the [after.html](./after.html) file.

</details>

## Resources

- [WCAG 2.4.4 Link Purpose (In Context)](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context)
- [WCAG 2.4.9 Link Purpose (Link Only)](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-link-only)
- [How to use aria-label on link](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA8)
- [Providing descriptive link text](https://www.w3.org/WAI/WCAG21/Techniques/general/G91)
- [`<a>` tag docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
