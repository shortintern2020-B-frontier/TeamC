<!-- Author:Shun Kiyoura-->
<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center">
        <v-list three-line style="max-height: 500px" class="overflow-y-auto">
          <template v-for="room in rooms">
            <v-list-item true :key="room.chat_room_id" link :to="`/rooms/${room.id}`">
              <v-list-item-avatar>
                <v-img :src="avatar(room.users[0].id)"></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title v-html="room.users[0].username"></v-list-item-title>
                <v-list-item-subtitle v-html="room.last_chat.content"></v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-list>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
    async created() {
    const res = await this.$axios.get("/chat_rooms", {
      params: {
        id: this.$store.state.user.userInfo.id,
      },
    });
    this.rooms = res.data;
    console.log(this.rooms);
  },

  data: () => ({
    rooms: [],
    names: "",
    items: [
      { header: "Talk List" },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        },
      { divider: true, inset: true }
    ],
  }),
  methods: {
    nameCombine: function (name) {
      names += name;
    },
  },
  computed: {
    avatar() {
      return (id) => {
        const imageLen = 10;
        return `/user_icon_${id % imageLen + 1}.jpg`;
      }
    }
  }
};
</script>
