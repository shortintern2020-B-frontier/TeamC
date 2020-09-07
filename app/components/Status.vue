<template>
  <ul style="list-style: none;">
    <li v-for="item in items" :key="item.status">
      <div>
        <!-- アイコンに差し替え
        <img v-bind:src="item.src" />-->
        {{item.status}}
        <v-switch></v-switch>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { status: "Free", src: "@/static/icon/#" },
        { status: "Busy", src: "@/static/icon/#" },
      ],
    };
  },
};
</script>