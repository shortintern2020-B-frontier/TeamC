<!-- author Hiroki Okubo -->

<template>
  <v-app style="margin:5%;">
    <v-main>
      <form align="center">
        <h1 style="display: inline-block; text-align: center; margin: 0 auto;">タイムライン</h1>
        <v-text-field v-model="title" :counter="10" label="Title" required></v-text-field>
        <v-text-field v-model="place" :counter="10" label="Place" required></v-text-field>
        <Datetime
          v-model="event_date"
          :minute-interval="10"
          :format="'YYYY-MM-DD HH:mm'"
          :overlay="true"
          :min-date="start"
          :max-date="end"
        ></Datetime>
        <v-text-field v-model="comment" :counter="10" label="Comment" required></v-text-field>

        <v-btn class="mr-4" @click="submit">submit</v-btn>
        <v-btn @click="clear">clear</v-btn>
      </form>
    </v-main>
  </v-app>
</template>

<script>
// Author Shotaro Murata
import Datetime from "vue-ctk-date-time-picker";
import "@/node_modules/vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css";
export default {
  name: "timelinePost",
  components: { Datetime },
  data: () => ({
    title: "",
    place: "",
    event_date: "",
    comment: "",
  }),
  methods: {
    submit: async function () {
      const event_datetime = new Date(this.event_date).getTime();
      await this.$axios.$post("/users/timeline", {
        user_id: this.$store.state.user.userInfo.id,
        place: this.place,
        event_date: event_datetime,
        comment: this.comment,
      });
      this.$router.push("/timeline");
    },
    clear: function () {
      this.title = "";
      this.place = "";
      this.data = "";
      this.comment = "";
    },
  },
};
</script>
