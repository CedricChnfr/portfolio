---
layout: default
title: Confidentialité
permalink: /confidentialite/
nav_exclude: true
---

<style>
.pv-wrapper {
  max-width: 760px;
  margin: 0 auto;
  padding: 3rem 1.5rem 5rem;
  line-height: 1.7;
}
.pv-wrapper h1 {
  font-size: 1.9rem;
  margin-bottom: 1.2rem;
}
.pv-wrapper h2 {
  font-size: 1.2rem;
  margin-top: 2.2rem;
  margin-bottom: 0.6rem;
}
.pv-wrapper ul {
  padding-left: 1.3rem;
}
.pv-wrapper li {
  margin-bottom: 0.3rem;
}
.pv-wrapper a {
  word-break: break-all;
}
</style>

<div class="pv-wrapper">
  <h1 data-i18n="privacy-title">Vie privée &amp; statistiques de visite</h1>

  <p data-i18n="privacy-intro">Ce site collecte automatiquement quelques informations techniques à chaque visite, uniquement à des fins de suivi de fréquentation par l'auteur du site. Aucune de ces informations n'est utilisée pour vous identifier personnellement, établir un profil ou vous cibler publicitairement.</p>

  <h2 data-i18n="privacy-what-title">Quelles données sont collectées ?</h2>
  <ul>
    <li data-i18n="privacy-what-li-1">La page visitée et la page d'où vous venez (référent)</li>
    <li data-i18n="privacy-what-li-2">Une estimation de votre localisation (ville, pays) déduite de votre adresse IP</li>
    <li data-i18n="privacy-what-li-3">Le nom de votre fournisseur d'accès ou opérateur réseau</li>
    <li data-i18n="privacy-what-li-4">Votre adresse IP</li>
    <li data-i18n="privacy-what-li-5">Votre fuseau horaire et la langue de votre navigateur</li>
    <li data-i18n="privacy-what-li-6">Le type d'appareil (mobile / ordinateur), la résolution d'écran et le type de connexion</li>
  </ul>

  <h2 data-i18n="privacy-how-title">Comment ces données sont-elles utilisées ?</h2>
  <p data-i18n-html="privacy-how-text">À chaque chargement de page, un script interroge le service tiers <strong>ipapi.co</strong> pour estimer votre localisation à partir de votre adresse IP, puis envoie une notification via le service <strong>ntfy.sh</strong> à l'auteur du site pour l'informer de la visite. Aucun cookie ni identifiant persistant n'est déposé dans votre navigateur, et ces données ne sont pas utilisées pour vous reconnaître d'une visite à l'autre.</p>

  <h2 data-i18n="privacy-never-title">Ce qui n'est jamais collecté</h2>
  <p data-i18n="privacy-never-text">Votre nom, prénom, adresse e-mail, ou toute autre information permettant de vous identifier personnellement — sauf si vous nous la transmettez vous-même, par exemple en écrivant par e-mail.</p>

  <h2 data-i18n="privacy-rights-title">Vos droits</h2>
  <p><span data-i18n="privacy-rights-text">Conformément au RGPD, vous disposez d'un droit d'accès, de rectification et d'opposition concernant les données vous concernant. Vous pouvez exercer ce droit en écrivant à</span> <a href="mailto:{{ site.email }}">{{ site.email }}</a>.</p>
</div>
