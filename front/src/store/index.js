import { createStore } from 'vuex'
import HTTP from '@/api'
// import router from '@/router'

const store = createStore({
    state: {
        accessToken: null,
        refreshToken: null,
    },
    mutations: {
        setToken: (state, {access, refresh}) => {
            state.accessToken = access
            state.refreshToken = refresh

            // console.log('setTokne')
            // console.log(state.accessToken)
        },
        clearToken: (state) => {
            state.accessToken = null
            state.refreshToken = null
        }
    },
    getters: {
        isAuthenticated (state) {
            return state.accessToken != null && state.refreshToken != null
        }

    },
    actions: {
        SignIn: async ({ commit }, model) => {
            HTTP.post('api/token/', model)
            .then((res) => {
                commit('setToken', res.data)
                console.log('RECEIVED', res.data)
            })
        },
        SignOut: ({ commit }) => {
            commit('clearToken')
        }
    }
})

export default store
