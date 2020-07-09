<template>
  <div class="columns">
    <slot />
  </div>
</template>

<style scoped>
.columns {
    display: flex;
}

.columns > div {
    flex: 1;
}
</style>
