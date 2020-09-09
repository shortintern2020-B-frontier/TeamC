// Author: ZHANG CHI
<template>
  <v-app>
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4" align="center" justify="center">
            <v-avatar color="" size="62">
              <img src="~/static/v.png" alt="logo" />
            </v-avatar>
            <v-card-title class="layout justify-center" disabled="true">
              ようこそ～ゆるまっちへ
            </v-card-title>
            <v-spacer></v-spacer>
            <v-card>
              <v-card-text>
                <v-form ref="form" v-model="valid" :lazy-validation="lazy">
                  <v-text-field
                    v-model="username"
                    id="username"
                    label="UserName"
                    name="UserName"
                    prepend-icon="mdi-account"
                    type="text"
                    :rules="usernameRules"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="userid"
                    id="userid"
                    label="Userid"
                    name="Userid"
                    prepend-icon="mdi-account"
                    type="text"
                    :rules="useridRules"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="email"
                    id="email"
                    label="Email"
                    name="email"
                    prepend-icon="mdi-account"
                    type="text"
                    :rules="emailRules"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
                    label="password"
                    name="password"
                    prepend-icon="mdi-lock"
                    type="password"
                    :rules="passwordRules"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
            </v-card>
            <v-card-actions class="layout justify-center">
              <v-btn
                ref="register"
                large
                color="red"
                class="layout justify-center"
                @click="register"
              >
                新規作成
              </v-btn>
            </v-card-actions>
            <v-divider></v-divider>
            <v-card-actions>
              <v-btn
                small
                color="gray"
                class="layout justify-center"
                nuxt
                to="/login"
              >
                ログイン
              </v-btn>
            </v-card-actions>
            <v-card>
              アカウントを作成すると、利用規約、およびCookie使用を含むプライバシーポリシーに同意したことになります。あなたのメールアドレスを保存しているTwitterユーザに通知などが表示されます。
            </v-card>
            <v-snackbar v-model="snackbar">
              {{ text }}
            </v-snackbar>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  layout: "login",
  data: () => ({
    valid: true,
    lazy: false,
    username: "",
    usernameRules: [v => !!v || "UserName is required"],
    userid: "",
    useridRules: [v => !!v || "UserID is required"],
    email: "",
    emailRules: [
      v => !!v || "Email is required",
      v => /.+@.+\..+/.test(v) || "E-mail must be valid"
    ],
    password: "",
    passwordRules: [v => !!v || "Password is required"],
    snackbar: false,
    text: "Success,3s auto to login",
    timeout: 2000
  }),
  methods: {
    register() {
      if (this.$refs.form.validate()) {
        let _this = this;
        const { username, userid, email, password } = this;
        this.$axios({
          method: "post",
          url: "/users/create",
          data: {
            username: username,
            user_id: userid,
            email: email,
            password: password,
            status: 0,
            comment: ""
          }
        })
          .then(function(response) {
            _this.snackbar = true;
            setTimeout(() => {
              _this.$router.push("/login");
              //Timeout 3s
            }, 3000);
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    }
  }
};
</script>
