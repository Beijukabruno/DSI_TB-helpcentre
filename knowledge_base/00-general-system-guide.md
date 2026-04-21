# DSI MDR-TB System — General User Guide

This is the cross-cutting reference for everyone who uses the DSI MDR-TB platform. Whatever your role, start here to learn how to log in, find your way around, read error messages, and resolve common issues without calling a developer.

## Table of Contents

1. [What this system is for](#1-what-this-system-is-for)
2. [Supported devices and browsers](#2-supported-devices-and-browsers)
3. [Logging in](#3-logging-in)
4. [Resetting your password](#4-resetting-your-password)
5. [The sidebar and top header](#5-the-sidebar-and-top-header)
6. [Common UI patterns](#6-common-ui-patterns)
7. [Reading error messages](#7-reading-error-messages)
8. [Logging out](#8-logging-out)
9. [Frequently asked questions](#9-frequently-asked-questions)
10. [Where to get help](#10-where-to-get-help)

---

## 1. What this system is for

The DSI MDR-TB platform is a web application for managing patients with multi-drug-resistant tuberculosis across health facilities. It brings doctors, nurses, lab technicians, radiographers, radiologists, facility administrators, and super administrators into one shared workflow — from registering a new patient, to ordering tests, to capturing and reading X-ray images, to tracking treatment outcomes. Each role sees only the screens and data relevant to their job.

---

## 2. Supported devices and browsers

The system is designed to be **mobile-responsive**, so the same pages work on a laptop in a clinic and on a phone at a patient's bedside.

**Desktop / laptop**

- Google Chrome (latest)
- Mozilla Firefox (latest)

**Mobile**

- Android — Chrome
- iPhone / iPad — Safari

On smaller screens, tables automatically become **stacked cards** so you can still see every field without scrolling sideways. Buttons and tap targets are sized to at least 44 pixels so they are easy to tap on a phone.

---

## 3. Logging in

### Where to log in

1. Open your browser and go to the system URL provided by your facility administrator.
2. From the home page, click **Sign In** (top right) or **Get Started**.
3. You will land on the login screen titled `Welcome Back!`.

### What to enter

- **Username** — your assigned username (not your email).
- **Password** — your assigned password.
- Tap the **eye icon** on the right of the password field to show or hide what you typed.

Click **SIGN IN**. While the request is in progress the button changes to **SIGNING IN...**.

### What happens on success

You see a green toast in the bottom-right corner that says:

> **Login Successful** — Welcome back!

You are then automatically redirected to your role's dashboard:

| Role | You land on |
|------|-------------|
| Doctor | `/doctor` |
| Nurse | `/nurse` |
| Lab Technician | `/lab_technician` |
| Radiographer | `/radiographer` |
| Radiologist | `/radiologist` |
| Facility Admin | `/facility_admin` |
| Super Admin | `/super_admin` |

### What happens on failure

A red banner appears at the top of the form and a red toast in the bottom-right. The wording depends on what went wrong:

- **Invalid Credentials** — "The username or password you entered is incorrect." Check for typos and Caps Lock, then try again.
- **Invalid Request** — Your input was rejected. Re-check the username and password fields.
- **Access Denied** — "Your account does not have permission to log in." Contact your facility administrator.
- **Account Not Found** — "No account exists with these credentials." Confirm with your administrator that the account was created.
- **Server Error** — "Our servers are experiencing issues. Please try again later." Wait a minute and retry.

### "Network Error"

If you see **No Internet Connection** or **Network Error**, your device cannot reach the server. This is almost always a connectivity problem on your side:

1. Check that your Wi-Fi or mobile data is on.
2. Try opening any other website.
3. If other sites work but this one doesn't, wait a minute and try again.
4. If it keeps failing, contact your administrator.

### "Session Expired"

If you have been logged in for a long time and your access token expires, the system shows a red toast:

> **Session expired** — Please log in again to continue.

You will be returned to the login page. This is normal — log in again and continue where you left off.

---

## 4. Resetting your password

If you have forgotten your password, you do **not** need to ask an administrator first — you can reset it yourself by email.

1. On the login page, click **Forgot Password?** (next to the password field).
2. You are taken to the **Reset Password** page.
3. Enter the **email address** linked to your account.
4. Click **Send Reset Instructions**. The button changes to **Sending...** while the request runs.

### What "Check your email" tells you

On success you see a confirmation screen with a green check mark and the heading **Check your email**. Below it the system displays the email address you entered and reminds you:

> Didn't receive the email? Check your spam folder or try again.

From here you can:

- Click **Try another email** — return to the form to enter a different address.
- Click **Back to login** — return to the login page.

Open your email and follow the link inside. The link expires after a short time, so use it quickly.

### What to do if the email doesn't arrive

1. Wait 1–2 minutes — email is not always instant.
2. Check your **Spam** or **Junk** folder.
3. Confirm you typed the email address correctly. If unsure, click **Try another email**.
4. If you still see nothing, common error toasts and what they mean:
   - **No account found with this email address** — the email is not registered. Contact your facility administrator.
   - **Password reset already requested** — a reset is already in progress for this email. Use that email or wait.
   - **Too many requests** — you tried too often. Wait a few minutes and try again.
   - **Service unavailable** — the server is temporarily down. Try again later.
5. If nothing works, contact your facility administrator and ask them to reset your password manually.

---

## 5. The sidebar and top header

Once you log in, every screen uses the same layout: a **sidebar** on the left and a **sticky header** along the top. The header stays visible while you scroll the page underneath it.

### The sidebar

The sidebar is on the left. Its menu items depend on your role — see your role-specific manual for the full list. Every role's sidebar contains:

- A **Dashboard** link at the top.
- **Settings** near the bottom.
- A **Log Out** button at the very bottom.

Each menu item shows an icon and a label. The currently active page is highlighted.

**On phones and tablets**, the sidebar is hidden by default to save screen space. Tap the **menu (hamburger)** icon in the top-left of the header to open it. A dark overlay appears behind the sidebar — tap the overlay, the **X** button, or press **Escape** to close it.

**On desktops**, you can collapse and expand the sidebar using the small arrow button on the left edge of the header.

### The top header

The header shows, from left to right:

- The **page title** of the screen you are on.
- A **menu toggle** (visible on small screens or when the sidebar is collapsed).
- The **notification bell** with an unread count badge.
- Your **profile avatar and name**.

### The notifications bell

1. Click the **bell icon** in the header.
2. A panel opens listing your notifications, grouped by **Today**, **Yesterday**, and **Earlier**.
3. The red badge on the bell shows how many are unread. If you have more than 9, it shows `9+`.
4. **Click a single notification** to mark it as read — the blue background highlight disappears.
5. Click **Mark All as Read** at the bottom of the panel to clear every unread indicator at once.
6. If you have no notifications, the panel shows the message **No notifications**.

### The profile menu

1. Click your avatar or name in the top-right of the header.
2. A small dropdown opens labelled **My Account**.
3. Choose **Settings** to go to your profile and preferences page.
4. Choose **Log Out** to end your session.

---

## 6. Common UI patterns

These patterns are used everywhere in the system. Recognising them will save you time.

- **Shimmer placeholders** — When a page is loading data from the server, you will see soft grey shapes pulsing where the content will appear. This means the system is working. **Wait for it — do not refresh the page.** Refreshing only restarts the wait.
- **Empty-state screens** — When a list (patients, test orders, notifications, etc.) has no items yet, the system shows an illustration with a short message telling you what to do next, for example *"No patients have been added yet."* This is normal and not an error.
- **Mobile cards** — On a phone, wide tables turn into **stacked cards**. Each card shows the same fields as a row would, just laid out vertically. Scroll up and down to see them all.
- **Date and time in your local timezone** — All dates and times are now displayed in your device's local timezone. (Previously the system showed times that were 3 hours off because backend timestamps were misread; this has been fixed. A visit you create at 11:00 AM will display as 11:00 AM.)
- **Sticky header** — The top header stays in place as you scroll, so the page title, notification bell, and profile menu are always reachable.
- **44 px tap targets** — All buttons, icons, and menu items on mobile are at least 44 × 44 pixels so they are easy to tap accurately.
- **Toast notifications** — Short messages appear in the **bottom-right corner** of the screen. **Green** toasts confirm a success (e.g. "Profile Updated Successfully"). **Red** toasts report an error (e.g. "Invalid Credentials"). They disappear after a few seconds — you do not need to dismiss them.
- **Status badges** — Coloured pill-shaped labels show status at a glance: green for completed/negative, amber for pending or in-progress, red for incomplete or positive, blue for primary actions, grey for unknown.

---

## 7. Reading error messages

Error messages in the system have been deliberately rewritten in plain language. When a server error happens, the original technical message is translated into a user-friendly version before it reaches you. The table below is the canonical reference — it shows the exact wording you may see, what it really means, and what to do next.

### Form and validation errors

| What you see | What it means | What to do |
|---|---|---|
| **Please check your input** + *"Please enter the test name when selecting 'Other'."* | You picked **Other** in a test type dropdown but did not type the custom name. | Type the name of the test in the text box that appeared next to the dropdown. |
| *"Please choose Yes or No for this field."* | A Yes/No radio button was left blank. | Select either Yes or No before submitting. |
| *"Please enter a valid number."* | A number field is empty or contains letters or symbols. | Enter digits only (e.g. `42`, not `forty-two`). |
| *"A required selection is missing. Please pick an option from the list."* | A dropdown that needed a value was left empty. | Open the dropdown and choose an item. |
| *"This field is required."* | A required text or input field is empty. | Fill it in before clicking submit. |

### Account and profile errors

| What you see | What it means | What to do |
|---|---|---|
| *"Your account isn't fully set up yet. Please contact your administrator."* | Your username exists in the login system but your application profile has not been created yet. | Contact your facility administrator and ask them to finish creating your profile. |
| *"We couldn't find your doctor profile. Please contact your administrator."* | Same as above, but specifically for doctor accounts. | Contact your facility administrator. |
| **User Profile Not Found** | The system couldn't load your `users/me` profile after login. | Log out and back in. If it persists, contact your administrator. |

### Data and record errors

| What you see | What it means | What to do |
|---|---|---|
| *"No patients are linked to your account yet."* | Your patient list is genuinely empty — no one has been assigned to you. | If you expect patients to be there, ask the nurse or admin who registers them to assign them to you. |
| *"We couldn't load your facility information. Please try again."* | The system failed to fetch facility details. | Click again or refresh once. If it keeps failing, contact your administrator. |
| *"The patient record could not be found."* | You followed a stale link or bookmark to a patient that no longer exists. | Go back to the patient list and pick the patient again. |
| *"The selected visit could not be found."* | A stale link to a visit that has been deleted or moved. | Refresh, go back to the visits list, and pick the visit again. |
| **Not Found** | A resource on the page could not be loaded. | Refresh once. If it persists, navigate from the dashboard rather than from a bookmark. |

### Connection and session errors

| What you see | What it means | What to do |
|---|---|---|
| **Network Error** / **No Internet Connection** | Your device cannot reach the server. | Check Wi-Fi or mobile data. Try opening another website to confirm. Retry. |
| **Session Expired** / **Session expired** | Your login token expired due to inactivity. | Log in again. Your work-in-progress data may not have been saved. |
| **Access Denied** | You tried to do something your role is not allowed to do. | This usually means a stale link. Use the sidebar to navigate to a screen that belongs to your role. |
| **Server Error** / **Something went wrong** | The server had a problem on its end. | Wait a minute and try again. If it keeps happening, contact your administrator. |
| **Service Unavailable** | The system is temporarily offline (often during deployment). | Wait a few minutes and try again. |

If you ever see a red toast whose wording is not in this table, the message itself describes what to do. Read it carefully — it is written for you, not for a developer.

---

## 8. Logging out

You can log out in two ways:

**From the sidebar**

1. Scroll to the bottom of the sidebar.
2. Click the **Log Out** button (with the door-arrow icon).

**From the profile menu**

1. Click your avatar or name in the top-right of the header.
2. Click **Log Out** in the dropdown.

When you log out, the system clears all stored login tokens and cached data on your device, then returns you to the login page. The next person to use the device will not see your data.

---

## 9. Frequently asked questions

**I forgot my password — what do I do?**
Use the **Forgot Password?** link on the login page. Enter your email and follow the link in the message you receive. See section 4 for the full walkthrough. If the email never arrives, contact your facility administrator.

**I logged in but I see "Your account isn't fully set up yet" — what now?**
Your login credentials work, but your application profile (the record that links you to a facility and a role) has not been created. Contact your **facility administrator** and ask them to complete your account setup. There is nothing you can fix on your end.

**The visit I created at 11 AM is showing 8 AM — is this fixed?**
Yes. Times are now displayed in your local timezone. The 3-hour offset bug — caused by treating server times as local instead of UTC — has been corrected. If you still see a wrong time on a specific page, report it as a bug.

**Why does the page show a shimmer effect when loading?**
The shimmer means the system is fetching data from the server. It is a normal loading indicator — wait for it to finish. **Do not refresh the page**, because that just restarts the wait.

**Why are the columns of a table not visible on my phone?**
On small screens, tables are converted to **stacked cards** to avoid horizontal scrolling. Each card contains the same fields as a row would. Scroll vertically to see all the records.

**What is DICOM?**
DICOM is the standard file format for medical imaging (like X-rays). Radiographers upload DICOM files into the system, and radiologists open them to write reports.

**I see "Network Error" but my internet works — what now?**
This usually means the server itself, not your connection, is unreachable. Wait one minute and try again. If other websites work but this one keeps showing Network Error, contact your facility administrator — the server may be down.

**Why did the system suddenly send me back to the login page?**
Your session expired. This is normal after a long period of inactivity. Log in again to continue.

**Where is the language setting?**
Open **Settings** from the profile menu or sidebar and choose **Language Preferences**. Currently only English is available; more languages are planned.

---

## 10. Where to get help

- **Account problems** (cannot log in, profile incomplete, password not working, wrong role): contact your **facility administrator**.
- **Facility-level problems** (whole facility cannot log in, server outage): your facility administrator should escalate to the **super administrator**.
- **Bugs and broken pages**: file a bug report with your administrator. Include:
  1. What you were trying to do.
  2. The exact error message you saw (a screenshot is best).
  3. The page URL from your browser address bar.
  4. The date and time it happened.

This guide covers behaviour shared by every role. For step-by-step instructions on the screens specific to your job, see the role manual for **Doctor**, **Nurse**, **Lab Technician**, **Radiographer**, **Radiologist**, **Facility Admin**, or **Super Admin**.
