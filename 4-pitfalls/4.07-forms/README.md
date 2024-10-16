# 4.7. Forms

In this exercise, your goal is to improve the accessability of the form on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.07-forms/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.07-forms/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

Support tools:

- Screen reader
- Color blindness simulation

## Hints

<details>
<summary>Hint 1</summary>

Try to locate the form controls using the screen reader.

- Mac: <kbd>VO + Cmd + J</kbd>
- Windows: <kbd>F</kbd>
- Android: <kbd>Swipe up + down</kbd> to choose form fields navigation. Then <kbd>Swipe down/up</kbd>.
- Android: <kbd>Twisting</kbd> to choose form fields navigation. Then <kbd>Swipe down/up</kbd>.

</details>

<details>
<summary>Hint 2</summary>

Try to select checkboxes and radios using the screen reader.

</details>

<details>
<details>
<summary>Hint 3</summary>

Turn on color blindness simulation in the browser. Then try to locate form controls with errors.

</details>
<details>
<summary>Hint 4</summary>

Focus form control with error using screen reader. Is the control announced differently then the control without error?

</details>

<details>
<summary>Hint 5</summary>

Try to distinguish required form fields using screen reader.

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

There is no connection between form fields and labels. Thus screen reader cannot read the label for the form field and announces it as "edit text".

</details>
<details>
<summary>Solution for problem 1</summary>

You need to connect the form field with the label. You can do it in three ways:

- Use `for` attribute in the label and `id` attribute in the form field.
  ```html
  <label for="name">Name</label> <input type="text" id="name" name="name" />
  ```
- Wrap the form field with the label.
  ```html
  <label>
    Name
    <input type="text" name="name" />
  </label>
  ```
- Use `aria-labelledby` attribute in the form field.
  ```html
  <label id="name-label">Name</label>
  <input type="text" aria-labelledby="name-label" name="name" />
  ```

</details>

<details>
<summary>Problem 2</summary>

The lack of connection between the form fields and the labels is even more problematic for checkboxes and radio buttons. There should be a connection between controls inside the group and the group label. Also the individual controls should be connected with the labels.

</details>
<details>
<summary>Solution for problem 2</summary>

1. Radio buttons and checkboxes should be connected with the labels - all of the solutions from the previous problem can be used, but the best experience is when the form field is wrapped with the label.
   ```html
   <label>
     <input type="checkbox" name="monday" />
     Monday
   </label>
   ```
2. The group of checkboxes should be connected via list and group
   ```html
   <label id="office-days-label">When do you come to the office?</label>
   <div role="group" class="checkbox-group">
     <ul aria-labelledby="office-days-label" class="checkbox-group">
       <li>
         <label>
           <input type="checkbox" name="monday" />
           Monday
         </label>
       </li>
       ...
     </ul>
   </div>
   ```
3. The group of radios should be connected to the group label, by using `aria-labelledby` attribute
   ```html
   <label id="gender-list-label">Gender</label>
   <div
     aria-labelledby="gender-list-label"
     role="radiogroup"
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

The `Password` input only displays error message when it is focused. Otherwise the only indication of the problem is a red border around the input. When user has a color blindness, they may not see the red border.

</details>
<details>
<summary>Solution for problem 3</summary>

You can:

- Always display the error message.
- Signal the error using other visual cues, like an icon

In the `before.html` file, you need to remove `fancy-error` class from the password's error `span`

```diff
- <span class="error fancy-error">This field is required</span>
+ <span class="error">This field is required</span>
```

</details>

<details>
<summary>Problem 4</summary>

When there is an error in the input, the screen reader does not announce it as invalid.

</details>
<details>
<summary>Solution for problem 4</summary>

Add `aria-invalid="true"` attribute to the input field(s) with an error. For example:

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

Required fields are only marked with visual cues (`*`). This may be a problem for screen reader users.

</details>
<details>
<summary>Solution for problem 5</summary>

There are at least two solutions to this problem:

- Use `aria-required` attribute on the form field. This will only add the required attribute without the browser validation.
  ```html
  <input type="password" id="password" aria-required="true" />
  ```
  - In this case it may be also useful to wrap `*` with `aria-hidden="true"` attribute to hide it from the screen reader.
    ```html
    <label for="password"> Password<span aria-hidden="true">*</span> </label>
    ```
- Use `required` attribute on the form field. This will also add browser validation, but it will display a default error message.
  ```html
  <input type="password" id="password" required="true" />
  ```

</details>

## Resources

https://www.smashingmagazine.com/2023/02/guide-accessible-form-validation/

https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/examples/checkbox/

https://www.w3.org/WAI/ARIA/apg/patterns/radio/

TODO: Resources
