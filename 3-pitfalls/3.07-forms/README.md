# 3.7. Forms

In this exercise, your goal is to improve the accessibility of the **form** on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/3-pitfalls/3.07-forms/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/3-pitfalls/3.07-forms/before.html)
- [source code](./before.html)

You can compare your solutions with the [after.html](after.html) file.

If you prefer not to solve the problems yourself, you can use the solution files to explore how each issue was fixed and look for any remaining problems:

- [Solution after problem 1](https://ubax.github.io/a11y-kata/3-pitfalls/3.07-forms/after-problem-1.html)
- [Solution after problem 2](https://ubax.github.io/a11y-kata/3-pitfalls/3.07-forms/after-problem-2.html)
- [Solution after problem 3](https://ubax.github.io/a11y-kata/3-pitfalls/3.07-forms/after-problem-3.html)
- [Solution after problem 4](https://ubax.github.io/a11y-kata/3-pitfalls/3.07-forms/after-problem-4.html)
- [Solution after all problems](https://ubax.github.io/a11y-kata/3-pitfalls/3.07-forms/after.html)

## Hints

<details>
<summary>Hint 1</summary>

Try to locate the form controls using a screen reader:

- Mac: <kbd>VO + Cmd + J</kbd>
- Windows: <kbd>F</kbd>
- Android: <kbd>Swipe up + down</kbd> to select form fields navigation, then <kbd>swipe down/up</kbd>.
- iOS: <kbd>Twisting</kbd> to select form fields navigation, then <kbd>Swipe down/up</kbd>.

Can you understand what is the name of the field?

</details>

<details>
<summary>Hint 2</summary>

Try selecting checkboxes and radio buttons using a screen reader. Can you hear the names for each option?

</details>

<details>
<summary>Hint 3</summary>

Enable color blindness simulation in your browser and try to locate form controls with errors.

Refer to [2.3 Disability simulation - Color blindness](../../2-tools/2.3-disability-simulation.md#exercise-1-simulating-color-blindness) for instructions on how to disable colors in the browser.

</details>

<details>
<summary>Hint 4</summary>

Focus on a form control with an error using a screen reader. Is it announced differently from a regular control?

</details>

<details>
<summary>Hint 5</summary>

Try to distinguish required fields using a screen reader.

</details>

## Problems & Solutions

<details>
<summary>Problem 1</summary>

Form fields are not properly associated with their labels, making it difficult for screen readers to identify them. They are announced as "edit text" instead of with the field's label. [WCAG 3.3.2 - Labels or Instructions](https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions.html)

</details>
<details>
<summary>Solution for problem 1</summary>

Associate each form field with its label by:

- Using the `for` attribute on the label and the `id` attribute on the form field.
  ```diff
  - <label>Name</label> <input type="text" id="name" name="name" />
  + <label for="name">Name</label> <input type="text" id="name" name="name" />
  ```
- Wrapping the form field with the label.
  ```diff
  - <label>Name</label> <input type="text" id="name" name="name" />
  + <label>
  +  Name
  +  <input type="text" name="name" />
  + </label>
  ```
- Using the `aria-labelledby` attribute on the form field.
  ```diff
  - <label>Name</label>
  + <label id="name-label">Name</label>
  - <input type="text" name="name" />
  + <input type="text" aria-labelledby="name-label" name="name" />
  ```

</details>

<details>
<summary>Problem 2</summary>

The issue is more significant for checkboxes and radio buttons, as there's no connection between individual controls, group labels, and controls within a group.

</details>
<details>
<summary>Solution for problem 2</summary>

1. Connect radio buttons and checkboxes with their labels. The best experience is to wrap the form field with the label.
   ```html
   <label>
     <input type="checkbox" name="monday" />
     Monday
   </label>
   ```
2. Group checkboxes using a list and group them properly.
   ```diff
   <label id="office-days-label">When do you come to the office?</label>
   <div role="group" class="checkbox-group">
   +  <ul aria-labelledby="office-days-label" class="checkbox-group">
   -  <input type="checkbox" name="monday" />
   -  <label> Monday </label>
   +   <li>
   +     <label>
   +       <input type="checkbox" name="monday" />
   +       Monday
   +     </label>
   +   </li>
       ...
   +  </ul>
   </div>
   ```
3. Use the `aria-labelledby` attribute to associate radio button groups with their group labels.
   ```diff
   - <label>Gender</label>
   + <label id="gender-list-label">Gender</label>
   <div
   +  aria-labelledby="gender-list-label"
   +  role="radiogroup"
     class="radio-group"
   >
     <label>
       <input type="radio" name="gender" value="male" />
       Male
     </label>
     ...
   </div>
   ```

</details>

<details>
<summary>Problem 3</summary>

The `Password` input only displays an error message when it's focused. The error is also indicated by a red border, which may not be visible to users with color blindness. [WCAG 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color)

</details>
<details>
<summary>Solution for problem 3</summary>

To fix this:

- Always display the error message.
- Use additional visual cues, such as an icon.

In the `before.html` file, remove the `fancy-error` class from the password’s error `span`.

```diff
- <span class="error fancy-error">This field is required</span>
+ <span class="error">This field is required</span>
```

</details>

<details>
<summary>Problem 4</summary>

When an input field contains an error, the screen reader does not announce it as invalid. [WCAG 3.3.1](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)

</details>
<details>
<summary>Solution for problem 4</summary>

Add the `aria-invalid="true"` attribute to the input field(s) with an error. For example:

```js
if (!email.value) {
  ...
  email.ariaInvalid = true;
} else {
  ...
  email.ariaInvalid = false;
}
```

</details>

<details>
<summary>Problem 5</summary>

Required fields are only marked with a visual cue (an asterisk `*`), which screen reader users may not detect.

</details>
<details>
<summary>Solution for problem 5</summary>

There are two possible solutions:

- Use the `aria-required` attribute on the form field, which adds the required state without triggering browser validation.
  ```diff
  - <input type="password" id="password" />
  + <input type="password" id="password" aria-required="true" />
  ```
- Use the `required` attribute on the form field, which adds browser validation and displays a default error message.
  ```diff
  - <input type="password" id="password" />
  + <input type="password" id="password" required="true" />
  ```

</details>

## Resources

- [W3C Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/)
- [A Guide to Accessible Form Validation](https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/)
- [Checkbox - ARIA Design Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/examples/checkbox/)
- [Radio - ARIA Design Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/radio/)
