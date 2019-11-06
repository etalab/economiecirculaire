<template>
    <div class="row">
        <Dataset v-for="dataset in items" :slug="dataset" />
    </div>
</template>

<script>
export default {
    props: ['items']
}
</script>
