<template>
  <section class="section">
    <div class="container">
      <slot name="title" />
      <slot name="description" />
      <slot />
    </div>
  </section>
</template>

<style>
.row > * {
    flex: 1 1 0;
}
</style>
