// Author TomuHirata
export default function ({ redirect, store }) {
  if(!store.state.user.userInfo.id) {
    redirect('/login');
  }
}
