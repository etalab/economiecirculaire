<template>
  <ul>
    <li
      v-for="page in pages"
      :key="page.path"
    >
      <router-link :to="page.path">
        {{ page.title }}
      </router-link>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['dir'],
  data () {
    return {
      pages: []
    }
  },
  created () {
    this.pages = this.getPages()
  },
  methods: {
    getPages () {
      const currentPage = this.dir ? this.dir : this.$page.path

      const pages = this.$site.pages
        .filter(x => {
          return x.path.match(new RegExp(`(${currentPage})(?=.*html)`))
        })
        .sort((a, b) => {
          return new Date(b.frontmatter.date) - new Date(a.frontmatter.date)
        })

      return pages
    }
  }
}
</script>
