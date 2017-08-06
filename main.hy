(import asyncio

        discord
        [discord.ext [commands]])


(setv client (.Bot commands
                   :command-prefix ""
                   :description "Hi! I'm a bot.")
      rude-people [122122926760656896 103675685343612928])

#@((. client event)
   (. asyncio coroutine)
   (defn on-message [message]
     (yield-from (.send message.channel
                        (.format "fuck you {.author.mention}"
                                 message)))
     (when (in (. message author id)
               rude-people)
       (yield-from (.send message.channel
                          "double fuck you")))))

#@((.command client)
   (. asyncio coroutine)
   (defn load [ctx what]
     "Load a module"
     (try
      (.load-extension bot what)
      (except [ImportError]
        pass))))

#@((.command client)
   (. asyncio coroutine)
   (defn unload [ctx what]
     "Unload a module"
     (.unload-extension bot what)))

#@((.command client)
   (. asyncio coroutine)
   (defn hidethepainharoldandkillyourself [ctx]
     (yield-from (.logout bot))))

#@((.command client)
   (. asyncio coroutine)
   (defn status [ctx what]
     "Set status"
     (yield-from (.delete ctx.message))
     (when (.is-ready bot)
       (yield-from (.change-presence client :game (.Game discord
                                                  :name what))))))

#@((. client event)
   (. asyncio coroutine)
   (defn on-ready []
     (print "Yo boi! We up in dis, fam!")))

#@((. client event)
   (. asyncio coroutine)
   (defn on-command-error [ctx err]
     (when (instance? commands.CommandNotFound err)
       (yield-from (.send ctx (.format "{.invoked_with} is not a valid command"
                                       ctx))))))


(defmain [&rest args]
  pass
  (.run client "W10xv01289Gqw01tVas078510vASG07vb123tVa0sg701gv13t07va"))
