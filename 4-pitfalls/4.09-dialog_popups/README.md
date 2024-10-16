# 4.9. Dialogs & popups

In this exercise, your goal is to improve the accessability of the dialog on the page [before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.09-dialog_popups/before.html) ([source code](./before.html)).

You can refer to the [after-1.html](after-1.html) and [after-2.html](after-2.html) files to compare your solutions.

This exercise includes a special solution to all problems. Make sure to check it out after checking individual problems' solutions.

TODO: Add hints

<details>
<summary>Problem 1</summary>

When the dialog is opened, the focus is not automatically set to the button inside the dialog. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#:~:text=When%20a%20dialog%20opens%2C%20focus%20moves%20to%20an%20element%20contained%20in%20the%20dialog)

</details>
<details>
<summary>Solution for problem 1</summary>

With the current implementation, the easiest way to focus the button in the dialog is:

1. Add `autofocus` attribute to the button element.
   ```html
   <button autofocus class="primary-button" id="accept-cookies">Accept</button>
   ...
   <button autofocus class="primary-button" id="close-ingredients">
     Close
   </button>
   ```
2. Add focus method to `afterOpenDialog`
   ```diff
   function afterOpenDialog(dialog) {
   +  dialog.querySelector("[autofocus]")?.focus();
   }
   ```

Alternatively, you can just focus first button in the dialog after opening it.

```diff
function afterOpenDialog(dialog) {
+  dialog.querySelector("button")?.focus();
}
```

</details>

<details>
<summary>Problem 2</summary>

Focus is not kept (not trapped) inside the dialog when it is open. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#:~:text=Like%20non%2Dmodal%20dialogs%2C%20modal%20dialogs%20contain%20their%20tab%20sequence)

</details>
<details>
<summary>Solution for problem 2</summary>

To solve this issue we can use the `inert` attribute.

1. Add a function to modify the `inert` attribute of all elements outside the dialog.
   ```js
   function setInertOfContent(value) {
     Array.from(document.querySelector("body").children)
       .filter((child) => !child.classList.contains("dialog"))
       .forEach((element) => {
         element.inert = value;
       });
   }
   ```
2. Add `inert` attribute to all elements outside the dialog when the dialog is open.

   ```js
   function afterOpenDialog(dialog) {
        ...
        setInertOfContent(true);
        ...
    }
   ```

3. Remove `inert` attribute from all elements outside the dialog when the dialog is closed.
   ```js
   function beforeCloseDialog() {
        ...
        setInertOfContent(false);
        ...
   }
   ```

</details>

<details>
<summary>Problem 3</summary>

Focus does not return to the initial point. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#:~:text=When%20a%20dialog%20closes%2C%20focus%20returns%20to%20the%20element%20that%20invoked%20the%20dialog)

</details>
<details>
<summary>Solution for problem 3</summary>
    
To solve this issue we need to save the last focused element before opening the dialog and focus it after closing the dialog.
1. ```js
    let lastElementWithFocus = null;
    ...
    function beforeOpenDialog() {
        lastElementWithFocus = document.activeElement;
    }
    ```
2. ```js
    function afterCloseDialog() {
        lastElementWithFocus?.focus();
    }
    ```
</details>

<details>
<summary>Problem 4</summary>

Escape key does not close the dialog. [Specification](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/#keyboardinteraction)

</details>
<details>
<summary>Solution for problem 4</summary>

Add a function to close the dialog when the escape key is pressed. However we don't want to close the dialog when the cookie dialog is open.

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

Most of this issues can be solved by using html [`dialog`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) element. It simplifies the structure of the code and makes the custom logic unnecessary.

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
2.  Use [`showModal`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal) function to open the dialog
    ```diff
    function openDialog(dialog) {
        ...
    -    dialog.classList.add("open");
    +    dialog.showModal();
        ...
    }
    ```
3.  Use [`close`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close) function to close the dialog
    ```diff
    function closeDialog(dialog) {
        ...
        -    dialog.classList.remove("open");
        +    dialog.close();
        ...
    }
    ```
4.  Prevent the escape key from closing the dialog
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

https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog
