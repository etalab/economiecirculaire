<template>
    <div class="card">
        <div class="card__content">
            <slot />
        </div>
    </div>
</template>

<style>
.card {
    color: var(--theme-dark-text);
}

.card a, .card a:active, .card  a:focus, .card a:visited {
        text-decoration: underline;
        color: #0053b3;
        color: var(--theme-primary);
    }

.card a:hover {
    background-color: var(--lighter-grey);
}
</style>
