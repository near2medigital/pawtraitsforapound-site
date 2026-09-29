window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

const PAWTRAITS_ANALYTICS_KEY = 'pawtraits_analytics_consent';

function readPawtraitsAnalyticsConsent() {
  try { return localStorage.getItem(PAWTRAITS_ANALYTICS_KEY); }
  catch (e) { return null; }
}

function writePawtraitsAnalyticsConsent(value) {
  try { localStorage.setItem(PAWTRAITS_ANALYTICS_KEY, value); }
  catch (e) {}
}

gtag('consent', 'default', {
  analytics_storage: 'denied',
  ad_storage: 'denied',
  ad_user_data: 'denied',
  ad_personalization: 'denied'
});

if (readPawtraitsAnalyticsConsent() === 'granted') {
  gtag('consent', 'update', { analytics_storage: 'granted' });
}

gtag('js', new Date());
gtag('config', 'G-D6NKF31LLG');

document.addEventListener('DOMContentLoaded', function () {
  const banner = document.getElementById('analytics-consent');
  const accept = document.getElementById('analytics-accept');
  const decline = document.getElementById('analytics-decline');
  const settings = document.getElementById('cookie-settings');

  if (banner) banner.hidden = !!readPawtraitsAnalyticsConsent();

  if (accept) accept.addEventListener('click', function () {
    writePawtraitsAnalyticsConsent('granted');
    gtag('consent', 'update', { analytics_storage: 'granted' });
    if (banner) banner.hidden = true;
  });

  if (decline) decline.addEventListener('click', function () {
    writePawtraitsAnalyticsConsent('denied');
    gtag('consent', 'update', { analytics_storage: 'denied' });
    if (banner) banner.hidden = true;
  });

  if (settings) settings.addEventListener('click', function () {
    try { localStorage.removeItem(PAWTRAITS_ANALYTICS_KEY); } catch (e) {}
    gtag('consent', 'update', { analytics_storage: 'denied' });
    if (banner) banner.hidden = false;
  });
});
