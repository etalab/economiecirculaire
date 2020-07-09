const { description } = require('../../package')

module.exports = {
  dest: '../dist',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: "Les données de l'économie circulaire",
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,

  markdown: {
    anchor: { permalink: false }
  },

  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    ["link", {
        rel: "stylesheet",
        href: "https://unpkg.com/template.data.gouv.fr@1.3.2/dist/main.min.css"
    }],
    ["link", {
        rel: "shortcut icon",
        href: "https://static.data.gouv.fr/_themes/gouvfr/img/favicon.png"
    }]
  ],

  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    subdomain: 'economiecirculaire',
    apiUrl: process.env.VUE_APP_API_URL || 'http://localhost:5000/api',
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: false,
    nav: [
      {
        text: 'Guide',
        link: '/guide/',
      },
      {
        text: 'Config',
        link: '/config/'
      },
      {
        text: 'VuePress',
        link: 'https://v1.vuepress.vuejs.org'
      }
    ],
    sidebar: {
      '/guide/': [
        {
          title: 'Guide',
          collapsable: false,
          children: [
            '',
            'using-vue',
          ]
        }
      ],
    }
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
  ]
}
