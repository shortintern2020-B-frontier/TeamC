<!-- Author:Shun Kiyoura-->
<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center">
        <v-list style="max-height: 500px" class="overflow-y-auto">
          <template v-for="(message) in messages">
            <v-list-item true :key="message.content">
              <v-list-item-avatar>
                <v-img :src="items[1].avatar"></v-img>
              </v-list-item-avatar>
              <v-list-item-content > <!--style="height: 200px"-->
                <v-list-item-subtitle v-html="message.content"></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
        <v-text-field v-model="send_message" label="Message"></v-text-field>
        <v-btn @click="sendMessage">send</v-btn>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import Logo from "~/components/Logo.vue";
import VuetifyLogo from "~/components/VuetifyLogo.vue";

export default {
  components: {
    Logo,
    VuetifyLogo,
  },
  asyncData({ params }) {
    const { id } = params;
    return { chat_room_id: id };
  },
  async created() {
    const res = await this.$axios.get("/chats", {
      params: {
        chat_room_id: this.chat_room_id,
      },
    }); 
    this.messages = res.data;
  },
    methods: {
    sendMessage: async function () {
      console.log(this.send_message);
      await this.$axios.post("/chats/", {
        user_id: 1,//this.$store.state.user.userInfo.id,
        chat_room_id: this.chat_room_id,
        content: this.send_message
      });
    },
  },
  data: () => ({
    chat_room_id: 1,
    messages: [],
    items: [
      { header: "Chat" },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Brunch this weekend?",
        subtitle:
          "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
      },
      { divider: true, inset: true }
    ],
  }),
};
</script>
