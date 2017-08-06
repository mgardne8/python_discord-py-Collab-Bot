(import asyncio

        discord
        [discord.ext [commands]])

;; For future use
;; Do not modify unless you understand
;; (setv startup-extensions [])



(setv client (.Bot commands
                   :command-prefix ""
                   :description "Hi! I'm a bot.")
      ;; Make sure we have an overused and annoying prefix
      ;; Add useless description

      rude-people [122122926760656896 103675685343612928]) ;; devon and borked
      ;; Agreed

;; You must always be willing to lay your law down
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

;; Obligatory Load Command that gives no feedback
#@((.command client)
   (. asyncio coroutine)
   (defn load [ctx what]
     "Load a module"
     (try
      (.load-extension bot what)
      (except [ImportError]))))

;; Obligatory Unload Command that gives no feedback
#@((.command client)
   (. asyncio coroutine)
   (defn unload [ctx what]
     "Unload a module"
     (.unload-extension bot what)))

;; Everyone needs a command to disconnect their bot, let's make ours frustrating
#@((.command client)
   (. asyncio coroutine)
   (defn hidethepainharoldandkillyourself [ctx]
     (yield-from (.logout bot))))

;; Obligatory status editing command
#@((.command client)
   (. asyncio coroutine)
   (defn status [ctx what]
     "Set status"
     (yield-from (.delete ctx.message))
     (when (.is-ready bot)
       (yield-from (.change-presence client :game (.Game discord
                                                  :name what))))))

;; Obligatory on ready, make sure this gives a super inane message
#@((. client event)
   (. asyncio coroutine)
   (defn on-ready []
     (print "Yo boi! We up in dis, fam!")))

;; Obligatory notice when command not found
#@((. client event)
   (. asyncio coroutine)
   (defn on-command-error [ctx err]
     (when (instance? commands.CommandNotFound err)
       (yield-from (.send ctx (.format "{.invoked_with} is not a valid command"
                                       ctx))))))

;; Nice macro included with the language
(defmain [&rest args]

  ;; Obligatory token inclusion
  ;; Is this a real token?
  ;; I don't know, who is going to actually try it out?
  (.run client "W10xv01289Gqw01tVas078510vASG07vb123tVa0sg701gv13t07va"))
