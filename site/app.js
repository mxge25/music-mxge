'use strict';
const release = { published: false, tag: 'v1.0.0-beta.1-build.9' };
const companionRelease = { published: false, tag: 'mxge-loader-v0.6.0-beta.1' };
let language = 'ar';
let toastTimer;
const languageButton = document.querySelector('#language');
const toast = document.querySelector('#toast');
function notify(ar, en) {
  toast.textContent = language === 'ar' ? ar : en;
  toast.classList.add('visible');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('visible'), 4000);
}
function setLanguage(value) {
  language = value;
  document.documentElement.lang = value;
  document.documentElement.dir = value === 'ar' ? 'rtl' : 'ltr';
  for (const element of document.querySelectorAll('[data-ar][data-en]')) element.textContent = element.dataset[value];
  for (const element of document.querySelectorAll('[data-label-ar]')) element.setAttribute('aria-label', value === 'ar' ? element.dataset.labelAr : element.dataset.labelEn);
  languageButton.textContent = value === 'ar' ? 'English ↗' : 'العربية ↗';
  languageButton.lang = value === 'ar' ? 'en' : 'ar';
  languageButton.setAttribute('aria-label', value === 'ar' ? 'Switch to English' : 'التبديل للعربية');
  document.title = value === 'ar' ? 'MXGE Player — صوتك، على راحتك' : 'MXGE Player — Your audio. Your space.';
  toast.classList.remove('visible');
}
languageButton.addEventListener('click', () => setLanguage(language === 'ar' ? 'en' : 'ar'));
document.querySelector('#release-status').hidden = release.published;
document.querySelector('#companion-status').hidden = companionRelease.published;
for (const link of document.querySelectorAll('[data-asset]')) {
  const available = link.dataset.release === 'companion' ? companionRelease.published : release.published;
  if (!available) link.setAttribute('aria-disabled', 'true');
  link.addEventListener('click', event => {
    if (!available) {
      event.preventDefault();
      notify('جارٍ التحقق من ملفات هذا التطبيق على GitHub. جرّب لاحقًا.', 'The app’s GitHub release files are being verified. Please try again later.');
    }
  });
}
for (const button of document.querySelectorAll('[data-copy]')) button.addEventListener('click', async () => {
  const value = document.getElementById(button.dataset.copy).textContent.trim();
  try {
    await navigator.clipboard.writeText(value);
    notify('تم نسخ بصمة SHA256.', 'SHA256 checksum copied.');
  } catch (_) {
    const range = document.createRange();
    range.selectNodeContents(document.getElementById(button.dataset.copy));
    const selection = window.getSelection();
    selection.removeAllRanges(); selection.addRange(range);
    notify('تم تحديد البصمة؛ انسخها يدويًا.', 'Checksum selected; copy it manually.');
  }
});
