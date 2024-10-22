# 3.9. Dialogs & Popups

In this exercise, your goal is to improve the accessibility of the **dialogs** on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/3-pitfalls/3.09-dialog_popups/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/3-pitfalls/3.09-dialog_popups/before.html)
- [source code](./before.html)

You can compare your solutions with the provided examples in [after-1.html](after-1.html) and [after-2.html](after-2.html). There is also a final solution that fixes all issues.

If you prefer not to solve the problems yourself, you can use the solution files to explore how each issue was fixed and look for any remaining problems:

- [Solution after problem 1](https://ubax.github.io/a11y-kata/3-pitfalls/3.09-dialog_popups/after-problem-1.html)
- [Solution after problem 2](https://ubax.github.io/a11y-kata/3-pitfalls/3.09-dialog_popups/after-problem-2.html)
- [Solution after problem 3](https://ubax.github.io/a11y-kata/3-pitfalls/3.09-dialog_popups/after-problem-3.html)

## Hints

<details>
<summary>Hint 1</summary>

Try accepting cookies and closing the dialog using only the keyboard.

</details>

<details>
<summary>Hint 2</summary>

Try adding a pizza to the order.

</details>

<details>
<summary>Hint 3</summary>

Try adding two pizzas to the order.

</details>

<details>
<summary>Hint 4</summary>

Try closing the dialog after adding a pizza without using the close button. [Dialog keyboard interaction](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#keyboardinteraction)

</details>

## Problems & Solutions

<details>
<summary>Problem 1</summary>

When the dialog is open, the focus is not kept (trapped) inside it. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#:~:text=Like%20non%2Dmodal%20dialogs%2C%20modal%20dialogs%20contain%20their%20tab%20sequence)

</details>
<details>
<summary>Solution for problem 1</summary>

Use the `inert` attribute to trap focus.

1. Create a function to set the `inert` attribute on all elements outside the dialog.
   ```js
   function setInertOfContent(value) {
     Array.from(document.querySelector("body").children) // Get all children of the body
       .filter((child) => !child.classList.contains("dialog")) // Filter out the dialog
       .forEach((element) => {
         element.inert = value; // Set the inert attribute
       });
   }
   ```
2. Add the `inert` attribute when the dialog opens.
   ```js
   function afterOpenDialog(dialog) {
        ...
        setInertOfContent(true);
        ...
    }
   ```
3. Remove the `inert` attribute when the dialog closes.
   ```js
   function beforeCloseDialog() {
        ...
        setInertOfContent(false);
        ...
   }
   ```

</details>

<details>
<summary>Problem 2</summary>

When the dialog closes, focus doesn't return to the element that triggered it. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#:~:text=When%20a%20dialog%20closes%2C%20focus%20returns%20to%20the%20element%20that%20invoked%20the%20dialog)

</details>
<details>
<summary>Solution for problem 2</summary>

1. Save the last focused element before opening the dialog.
   ```js
   let lastElementWithFocus = null;
   function beforeOpenDialog() {
     lastElementWithFocus = document.activeElement;
   }
   ```
2. Restore focus after closing the dialog.
   ```js
   function afterCloseDialog() {
     lastElementWithFocus?.focus();
   }
   ```

</details>

<details>
<summary>Problem 3</summary>

When the dialog opens, focus is not automatically set inside it. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#:~:text=When%20a%20dialog%20opens%2C%20focus%20moves%20to%20an%20element%20contained%20in%20the%20dialog)

</details>
<details>
<summary>Solution for problem 3</summary>

You can either:

1. Use `autofocus`

   - Add the `autofocus` attribute to the button inside the dialog.

   ```html
   <button autofocus class="primary-button" id="accept-cookies">Accept</button>
   ...
   <button autofocus class="primary-button" id="close-ingredients">
     Close
   </button>
   ```

   - Add focus method to `afterOpenDialog`

   ```diff
   function afterOpenDialog(dialog) {
   +  dialog.querySelector("[autofocus]")?.focus();
   }
   ```

2. Alternatively, focus the first button after opening the dialog.
   ```diff
   function afterOpenDialog(dialog) {
     ...
   +  dialog.querySelector("button")?.focus();
   }
   ```

</details>

<details>
<summary>Problem 4</summary>

The escape key should close the dialog. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#keyboardinteraction)

</details>
<details>
<summary>Solution for problem 4</summary>

Add a keydown event listener to close the dialog on Escape, but prevent it from closing the cookie dialog.

```js
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    if (cookieDialog.classList.contains("open")) {
      event.preventDefault();
    } else if (ingredientsDialog.classList.contains("open")) {
      closeDialog(ingredientsDialog);
    }
  }
});
```

</details>

<details>
<summary>Solution to all above problems</summary>

Switching to the native HTML [`dialog`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) element simplifies solving all these issues.

1.  Change the `div` element to `dialog`
    ```diff
    ...
    - <div class="dialog" ...>
    -    <div class="content">
    + <dialog ...>
            ...
    -    </div>
    - </div>
    + </dialog>
    ...
    ```
2.  Use the [`showModal`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal) function to open the dialog
    ```diff
    function openDialog(dialog) {
        ...
    -    dialog.classList.add("open");
    +    dialog.showModal();
        ...
    }
    ```
3.  Use the [`close`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close) function to close the dialog
    ```diff
    function closeDialog(dialog) {
        ...
        -    dialog.classList.remove("open");
        +    dialog.close();
        ...
    }
    ```
4.  Prevent Escape key from closing the dialog
    ```js
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        if (cookieDialog.open) {
          event.preventDefault();
        }
      }
    });
    ```

</details>

## Resources

- [Modal Dialog - ARIA Design Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [Dialog element - MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
