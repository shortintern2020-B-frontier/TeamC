import colors from 'vuetify/es5/util/colors'

export default {
  /*
  ** Nuxt rendering mode
  ** See https://nuxtjs.org/api/configuration-mode
  */
  mode: 'spa',
  /*
  ** Nuxt target
  ** See https://nuxtjs.org/api/configuration-target
  */
  target: 'server',
  /*
  ** Headers of the page
  ** See https://nuxtjs.org/api/configuration-head
  */
  head: {
    titleTemplate: '%s - ' + process.env.npm_package_name,
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    script: [
      {

      }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Global CSS
  */
  css: [
    '@mdi/font/css/materialdesignicons.css'
  ],
  /*
  ** Plugins to load before mounting the App
  ** https://nuxtjs.org/guide/plugins
  */
  plugins: [
    { src: "~plugins/persistedstate.js" }
  ],
  /*
  ** Auto import components
  ** See https://nuxtjs.org/api/configuration-components
  */
  components: true,
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/vuetify',
    '@nuxtjs/axios',
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/pwa',
    '@nuxtjs/axios',
  ],
  manifest: {
    name: 'ゆるまっち',
    lang: 'ja',
    short_name: 'ゆるまっち',
    title: 'ゆるまっち',
    'og:title': 'ゆるまっち',
    description: 'ゆるまっち',
    'og:description': 'ゆるまっち',
    theme_color: '#ffffff',
    background_color: '#ffffff',
    icons: [{
      "src": "https://s1.ax1x.com/2020/09/10/wY6kk9.png",
      "type": "image/png",
      "sizes": "512x512"
    },{
      "src": "https://s1.ax1x.com/2020/09/10/wY6Pw4.png",
      "type": "image/png",
      "sizes": "256x256"
    },{
      "src": "https://s1.ax1x.com/2020/09/10/wY6iTJ.png",
      "type": "image/png",
      "sizes": "192x192"
    },{
      "src": "https://s1.ax1x.com/2020/09/10/wY6Ef1.png",
      "type": "image/png",
      "sizes": "144x144"
    }, {
      "src": "https://s1.ax1x.com/2020/09/10/wY6AYR.png",
      "type": "image/png",
      "sizes": "128x128"
    }]
  },
  workbox: {
    dev: true, //開発環境でもPWA
  },
  router: {
    extendRoutes(routes, resolve) {
      routes.push({
        name: 'notFound',
        path: '*',
        component: resolve(__dirname, 'pages/login.vue')
      })
    }
  },
  /*
  ** vuetify module configuration
  ** https://github.com/nuxt-community/vuetify-module
  */
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },
  /*
  ** Build configuration
  ** See https://nuxtjs.org/api/configuration-build/
  */
  build: {
  },
  axios: {
    baseURL: 'http://127.0.0.1:8000',
  },
}
