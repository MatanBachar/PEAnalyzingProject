# Matan Bachar - Cynet Project

# standard Analyzer that analyze the questions by looking for keywords in any one of them

from modules.analyzers import anlyzer
from modules.responses import timestamp, fileresources, filesize, imagebase, osversion, subsystem, targetmachine,\
    filesignatures, filesections, entrypoint


class CommonAnalyzer(anlyzer.Analyzer):

    @staticmethod
    def analyze(question):
        if "what" in question.lower() and "size" in question.lower():
            return filesize.FileSizeResponse()
        elif "how many" in question.lower() and "signatures" in question.lower():
            return filesignatures.FileSignaturesResponse()
        elif "how many" in question.lower() and "resources" in question.lower():
            return fileresources.FileResourcesResponse()
        elif "how many" in question.lower() and "sections" in question.lower():
            return filesections.FileSectionsResponse()
        elif "image base" in question.lower():
            return imagebase.FileImageBaseResponse()
        elif "entry point" in question.lower():
            return entrypoint.FileEntryPointResponse()
        elif "os" in question.lower() or "operation system" in question.lower():
            return osversion.FileRequiredOSResponse()
        elif "what" in question.lower() and "subsystem" in question.lower():
            return subsystem.FileSubsystemResponse()
        elif "what" in question.lower() and "target machine" in question.lower():
            return targetmachine.FileTargetMachineResponse()
        elif "when" in question.lower() and "created" in question.lower() or \
                ("what" in question.lower() and "compliation time" in question.lower()):
            return timestamp.TimestampResponse()
        else: return None






text = "What is the size of the file?"