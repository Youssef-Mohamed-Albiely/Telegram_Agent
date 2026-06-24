from langchain_core.messages import SystemMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel , Field


from langchain_core.prompts import (
    SystemMessagePromptTemplate as smpt,
    HumanMessagePromptTemplate as hmpt,
    ChatPromptTemplate as cpt,
    )
from Agent.initialize_llm import llm


class memory (BaseChatMessageHistory , BaseModel):
    messages : list[BaseMessage] = Field(default_factory=list)
    llm:ChatOpenAI = Field(default=ChatOpenAI)
    k : int = Field(default=10)

    def __init__(self,llm:ChatOpenAI , k:int):
        super().__init__(llm=llm , k=k)

    def add_message(self, message:BaseMessage) ->None :
        old_messages:list[BaseMessage] | None = None
        current_summary:SystemMessage | None = None

        if len(self.messages) > 0 and isinstance(self.messages[0] , SystemMessage):
            current_summary = self.messages.pop(0).content

        self.messages.append(message)

        if len(self.messages) > self.k:
            old_messages = self.messages[:-self.k]
            self.messages= self.messages[-self.k:]

            summary_prompt = cpt.from_messages([
                smpt.from_template(
                    "Given the existing conversation summary and the new messages, "
                    "generate a new summary of the conversation. Ensuring to maintain "
                    "as much relevant information as possible."
                    "If the existing conversation summary = None, summarize only the new messages."
                ),
                hmpt.from_template(
                    "existing conversation summary is:\n{current_summary}\n\n"
                    "new messages is: \n{old_messages}"
                )
            ])

            new_summary = self.llm.invoke(
                summary_prompt.format_messages(current_summary=current_summary,old_messages = old_messages)
            )

            self.messages = [SystemMessage(content=new_summary.content)] + self.messages


    def clear(self) ->None:
        self.messages = []
