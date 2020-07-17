<template>
  <div
    class="hero"
    role="banner"
  >
    <div class="hero__container">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.hero {
  background-image: url('/assets/img/bandeau.jpg');
  background-size: cover;
}

.hero__container > * {
  background-color: white;
  padding: 10px 1em;
}
</style>
