<template>
  <a v-bind:href="url" class="button" :class="_class">
    <slot />
  </a>
</template>

<script>
export default {
  props: {
    url: String,
    _class: String
  }
}
</script>
