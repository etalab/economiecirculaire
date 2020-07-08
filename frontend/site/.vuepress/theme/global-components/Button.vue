<template>
  <a v-bind:href="url" class="button">
    <slot />
  </a>
</template>

<script>
export default {
  props: {
    url: String
  }
}
</script>
