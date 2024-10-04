# Presentation on Abbreviations

## Overview:
The presentation explains common abbreviations in the field of accessibility.

### 1. A11y (Accessibility):
- **A11y** (pronounced: *ally*) is a shorthand for accessibility.
- **Definition of Accessibility**: Ensuring that all users, regardless of abilities, can access and use a product or service.

#### Examples (Top-left to Bottom-left):
- **John**: Using a phone in bright sunlight, struggling with screen visibility (situational).
- **Jane**: Blind, using assistive technologies (permanent).
- **Emma**: Using her phone while caring for her baby, with only one hand free (situational).
- **George**: Elderly, has difficulty reading small text (permanent).
- **Olivia**: On a bus, needing to watch videos for school (situational).
- **Alex**: Developer with a cast on one arm (temporary).

#### Types of Disabilities:
- **Situational**: Context-dependent (e.g., John and Olivia).
- **Temporary**: Short-term (e.g., Alex).
- **Permanent**: Long-term or lifelong (e.g., Jane and George).

**Key Point**: Almost everyone experiences some form of disability at some point.

---

### 2. WCAG (Web Content Accessibility Guidelines):
WCAG provides criteria for making web content accessible.

- **Example: Success Criteria 1.3.1 (Info and Relationships)**:
  - The first number refers to the **Principle**:
    - Four principles: **Perceivable**, **Operable**, **Understandable**, **Robust**.
      - **Perceivable**: Information must be available to users in ways they can perceive.
      - **Operable**: Users must be able to interact with the interface.
      - **Understandable**: Information and operation must be clear and simple.
      - **Robust**: Content should work with a variety of technologies.
  
  - The second number refers to the **Guideline**:
    - 13 guidelines across the principles. Example: Guideline 1.3 (Adaptability), ensures content can be presented in different ways without losing meaning. [Learn more](https://www.w3.org/WAI/WCAG21/Understanding/adaptable).

  - The third number refers to the **Success Criterion**:
    - Success Criterion 1.3.1 ensures that content structure and relationships are programmatically determinable or available in text format. [More info](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html).

  - **Conformance Levels**:
    - **Level A**: Minimum conformance (supports assistive tech).
    - **Level AA**: Standard conformance (provides better accessibility for most users).
    - **Level AAA**: Highest conformance (optimal accessibility).

---

### 3. EAA (European Accessibility Act):
- **The EAA** is a directive to make products and services more accessible to people with disabilities. [Learn more](https://ec.europa.eu/social/main.jsp?catId=1202)
  - Requires compliance with **EN 301 549**, a European standard based on WCAG 2.1.
  - Minimum compliance is **Level AA** (A + AA).
  - Applies to both public and private sectors.
  - Targets companies with more than 10 employees or over €2 million in turnover.
  - **Deadline**: June 2025.
  - **Fines**: Up to €500,000 or 18 months in prison (varies by country).

---

### 4. Kata Exercise:
- The kata is divided into three parts: **Tools**, **Testing**, and **Pitfalls**.
  - In the first half, focus on tools (keyboard navigation, screen readers), automated, and manual testing.
  - In the second half, focus on common pitfalls, identifying and solving issues in code. No need to implement fixes if you are uncomfortable with code—just identify the issues and propose solutions.
  - Tasks will be done in pairs.
  - For screen readers, one person starts with desktop, the other with mobile, then switch.
  - Document your observations, experiences, and issues during the exercise. There will be a discussion at the end.
